#!/usr/bin/env python3
"""generate_commands_v2.py - Generate a proper commands.py from extracted registry.

This version generates clean handler functions instead of raw elif blocks.
"""
import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(SCRIPT_DIR, '..')
REGISTRY = os.path.join(SCRIPT_DIR, 'commands_registry.json')
AI_PY = os.path.join(PROJECT_DIR, 'AI.py')
OUT = os.path.join(PROJECT_DIR, 'bin', 'datae', 'commands.py')

def main():
    with open(REGISTRY, encoding='utf-8') as f:
        data = json.load(f)

    with open(AI_PY, encoding='utf-8') as f:
        ai_lines = f.readlines()

    with open(os.path.join(SCRIPT_DIR, 'auto_commands.json'), encoding='utf-8') as f:
        auto = json.load(f)

    # Find handle_cmd start
    cmd_start = None
    for i, line in enumerate(ai_lines):
        if line.strip().startswith('def handle_cmd('):
            cmd_start = i
            break

    # Extract full elif blocks for manual commands
    # We need the ORIGINAL source to understand what each command does
    manual_keys = {k for k, v in data.items() if v['pattern'] not in ('try_print', 'direct_print', 'data_preview')}

    # Build a map of key -> raw elif block (as list of source lines)
    manual_raw = {}
    i = cmd_start + 1
    while i < len(ai_lines):
        s = ai_lines[i].strip()
        if s.startswith('def ') and not s.startswith('def handle_cmd'):
            break
        if s.startswith('elif cmd') or s.startswith('elif _lower'):
            block_start = i
            block_lines = [ai_lines[i]]
            j = i + 1
            # Find block end: next elif/else/def at same indent
            base_indent = len(ai_lines[i]) - len(ai_lines[i].lstrip())
            while j < len(ai_lines):
                js = ai_lines[j].rstrip()
                js_stripped = js.strip()
                if not js_stripped:
                    block_lines.append(js)
                    j += 1
                    continue
                j_indent = len(js) - len(js.lstrip())
                if j_indent <= base_indent and js_stripped:
                    if js_stripped.startswith('elif ') or js_stripped.startswith('else:') or (js_stripped.startswith('def ') and not js_stripped.startswith('def handle_cmd')):
                        break
                block_lines.append(js)
                j += 1
            block = '\n'.join(block_lines)
            # Find matching manual keys
            for mk in list(manual_keys):
                if ('"' + mk + '"') in s or ("'" + mk + "'") in s:
                    manual_raw[mk] = block
                    manual_keys.discard(mk)
            i = j
        else:
            i += 1

    # Now generate the output
    out = []
    out.append('"""commands.py - Command registry for AI.py v6.2.0.')
    out.append('')
    out.append('Auto-generated from AI.py elif chain.')
    out.append('Regenerate: python scripts/generate_commands_v2.py')
    out.append('"""')
    out.append('')
    out.append('# Auto-eligible command mappings: command_key -> function_name')
    out.append('try_print = ' + json.dumps(auto['try_print'], indent=4, ensure_ascii=False))
    out.append('')
    out.append('direct_print = ' + json.dumps(auto['direct_print'], indent=4, ensure_ascii=False))
    out.append('')
    out.append('data_preview = ' + json.dumps(auto['data_preview'], indent=4, ensure_ascii=False))
    out.append('')
    out.append('')
    out.append('def _try_print(fn_name, ns):')
    out.append('    try:')
    out.append('        print(ns[fn_name]())')
    out.append('    except Exception as _e:')
    out.append('        print(_e)')
    out.append('')
    out.append('')
    out.append('def _direct_print(fn_name, ns):')
    out.append('    print(ns[fn_name]())')
    out.append('')
    out.append('')
    out.append('def _data_preview(fn_name, ns):')
    out.append('    try:')
    out.append('        _d = ns[fn_name]()')
    out.append('        print("{}: {} entries. First:".format(fn_name, len(_d)))')
    out.append('        for _x in _d[:2]:')
    out.append('            print("  ", _x)')
    out.append('    except Exception as _e:')
    out.append('        print("Error:", _e)')
    out.append('')
    out.append('')

    # Write raw blocks as comments for reference, then write the actual handler
    out.append('#' + '=' * 70)
    out.append('# Manual command handlers')
    out.append('# These are complex commands that cannot be auto-generated.')
    out.append('# The raw source from AI.py is included as comments for reference.')
    out.append('#' + '=' * 70)
    out.append('')

    for mk in sorted(manual_raw.keys()):
        raw = manual_raw[mk]
        safe = re.sub(r'[^a-zA-Z0-9_]', '_', mk)
        out.append(f'# --- {mk} ---')
        # Add raw source as comment
        for line in raw.split('\n'):
            out.append('# ' + line.rstrip())
        out.append(f'def _m_{safe}(cmd, role, name, badge, ns):')
        out.append(f'    """Manual handler for: {mk}"""')
        # Write a placeholder that raises NotImplementedError
        out.append(f'    raise NotImplementedError("Manual handler needed for: {mk}")')
        out.append('')
        out.append('')

    out.append('')
    out.append('def build_registry(namespace, cmd, role, name, badge):')
    out.append('    """Build command registry. Call from handle_cmd."""')
    out.append('    reg = {}')
    out.append('    # Auto-eligible commands')
    out.append('    for _k, _fn in try_print.items():')
    out.append('        reg[_k] = lambda _fn=_fn, _ns=namespace: _try_print(_fn, _ns)')
    out.append('    for _k, _fn in direct_print.items():')
    out.append('        reg[_k] = lambda _fn=_fn, _ns=namespace: _direct_print(_fn, _ns)')
    out.append('    for _k, _fn in data_preview.items():')
    out.append('        reg[_k] = lambda _fn=_fn, _ns=namespace: _data_preview(_fn, _ns)')
    out.append('    # Manual handlers (placeholder - replace with real implementations)')
    out.append('    # TODO: Implement manual handlers')
    out.append('    return reg')
    out.append('')

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(f'Generated: {OUT}')
    print(f'Auto-eligible: {len(auto["try_print"]) + len(auto["direct_print"]) + len(auto["data_preview"])}')
    print(f'Manual handlers needed: {len(manual_raw)}')
    print(f'Missing keys: {sorted(manual_keys)[:10]}...')

if __name__ == '__main__':
    main()
