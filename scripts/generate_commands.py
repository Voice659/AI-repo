#!/usr/bin/env python3
"""generate_commands.py - Generate bin/datae/commands.py from extracted registry."""
import json
import os
import re
import sys

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

    # Read the auto_commands.json for auto-eligible mappings
    auto_path = os.path.join(SCRIPT_DIR, 'auto_commands.json')
    with open(auto_path, encoding='utf-8') as f:
        auto = json.load(f)

    # Get the function bodies for manual commands
    manual_keys = {k for k, v in data.items() if v['pattern'] not in ('try_print', 'direct_print', 'data_preview')}

    # Find handle_cmd start
    cmd_start = None
    for i, line in enumerate(ai_lines):
        if line.strip().startswith('def handle_cmd('):
            cmd_start = i
            break

    # Extract raw elif blocks for manual commands
    # We'll store the raw source lines for each manual command
    manual_blocks = {}
    i = cmd_start + 1
    while i < len(ai_lines):
        s = ai_lines[i].strip()
        if s.startswith('def ') and not s.startswith('def handle_cmd'):
            break
        if s.startswith('elif cmd') or (s.startswith('elif _lower')):
            # Collect this block
            block_lines = [ai_lines[i]]
            j = i + 1
            indent = len(ai_lines[i]) - len(ai_lines[i].lstrip())
            while j < len(ai_lines):
                js = ai_lines[j].strip()
                if js.startswith('elif cmd') or js.startswith('elif _lower') or js.startswith('else:') or (js.startswith('def ') and not js.startswith('def handle_cmd')):
                    break
                if js and (js[0].isalpha() or js[0] == '_' or js[0] == '#') and not js.startswith(' ') and not js.startswith('\t'):
                    # Check if it's at the same or lower indent
                    j_indent = len(ai_lines[j]) - len(ai_lines[j].lstrip())
                    if j_indent <= indent and js:
                        break
                block_lines.append(ai_lines[j])
                j += 1
            block = ''.join(block_lines)
            # Try to find matching keys
            for mk in manual_keys:
                # Simple heuristic: check if the key appears in the elif line
                if mk in s or ('"' + mk + '"') in s:
                    manual_blocks[mk] = block.rstrip()
            i = j
        else:
            i += 1

    # Generate output
    out = []
    out.append('"""commands.py - Command registry for AI.py v6.2.0.')
    out.append('')
    out.append('Auto-generated from AI.py elif chain. Do not edit by hand.')
    out.append('Regenerate: python scripts/generate_commands.py')
    out.append('"""')
    out.append('')
    out.append('# Auto-eligible command mappings: command_key -> function_name')
    out.append('# try_print: wrapped in try/except')
    out.append('# direct_print: called directly')
    out.append('# data_preview: data preview with first 2 entries')
    out.append('')
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
    out.append('        print("{} data: {} entries. First:".format(fn_name, len(_d)))')
    out.append('        for _x in _d[:2]:')
    out.append('            print("  ", _x)')
    out.append('    except Exception as _e:')
    out.append('        print("Error:", _e)')
    out.append('')
    out.append('')
    out.append('# Manual command handlers - these need custom logic')
    out.append('# Each is a function(cmd, role, name, badge, ns) -> None')
    out.append('')

    # Write manual handler functions
    for mk in sorted(manual_blocks.keys()):
        block = manual_blocks[mk]
        safe_name = mk.replace(' ', '_').replace('-', '_').replace(':', '_').replace('.', '_').replace('/', '_')
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', safe_name)
        out.append(f'def _h_{safe_name}(cmd, role, name, badge, ns):')
        out.append(f'    # Manual handler for: {mk}')
        # Indent the block properly
        for line in block.split('\n'):
            out.append('    ' + line)
        out.append('')
        out.append('')

    out.append('')
    out.append('def build_registry(namespace):')
    out.append('    """Build command registry from namespace (globals())."""')
    out.append('    reg = {}')
    out.append('    for _k, _fn in try_print.items():')
    out.append('        reg[_k] = lambda _fn=_fn, _ns=namespace: _try_print(_fn, _ns)')
    out.append('    for _k, _fn in direct_print.items():')
    out.append('        reg[_k] = lambda _fn=_fn, _ns=namespace: _direct_print(_fn, _ns)')
    out.append('    for _k, _fn in data_preview.items():')
    out.append('        reg[_k] = lambda _fn=_fn, _ns=namespace: _data_preview(_fn, _ns)')

    # Register manual handlers
    for mk in sorted(manual_blocks.keys()):
        safe_name = mk.replace(' ', '_').replace('-', '_').replace(':', '_').replace('.', '_').replace('/', '_')
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', safe_name)
        out.append(f'    reg["{mk}"] = lambda cmd=cmd, role=role, name=name, badge=badge, ns=namespace: _h_{safe_name}(cmd, role, name, badge, ns)')

    out.append('    return reg')
    out.append('')

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(f'Generated: {OUT}')
    print(f'Auto-eligible: {len(auto["try_print"]) + len(auto["direct_print"]) + len(auto["data_preview"])}')
    print(f'Manual handlers: {len(manual_blocks)}')

if __name__ == '__main__':
    main()
