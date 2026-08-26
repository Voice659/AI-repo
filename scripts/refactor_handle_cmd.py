#!/usr/bin/env python3
"""refactor_handle_cmd.py - Remove auto-eligible elifs from AI.py handle_cmd.

This script:
1. Reads AI.py
2. For each elif branch in handle_cmd, checks if it's in the auto registry
3. If auto-eligible, removes the entire elif block
4. If manual, keeps it
5. Adds dispatch_auto call at the top of handle_cmd
6. Writes ONLY the changed lines back (preserves the rest of AI.py)
"""
import json
import re
import os

AI_PY = os.path.join(os.path.dirname(__file__), '..', 'AI.py')
REGISTRY = os.path.join(os.path.dirname(__file__), 'commands_registry.json')

def main():
    with open(AI_PY, encoding='utf-8') as f:
        lines = f.readlines()

    with open(REGISTRY, encoding='utf-8') as f:
        registry = json.load(f)

    # Build set of auto-eligible command keys
    auto_keys = set()
    for k, v in registry.items():
        if v['pattern'] in ('try_print', 'direct_print', 'data_preview'):
            clean = k.strip()
            if clean and '"' not in clean and ' and ' not in clean and ' or ' not in clean:
                auto_keys.add(clean)

    # Find handle_cmd start/end
    cmd_start = None
    cmd_end = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def handle_cmd('):
            cmd_start = i
        if cmd_start and i > cmd_start and line.strip().startswith('def ') and not line.strip().startswith('def handle_cmd'):
            cmd_end = i
            break

    if cmd_start is None:
        print("ERROR: handle_cmd not found")
        return

    print(f"handle_cmd: L{cmd_start+1}-L{cmd_end}")

    # Process handle_cmd: rebuild it from scratch
    new_cmd_lines = []

    # Copy the function header (def handle_cmd + registry check)
    i = cmd_start
    while i < cmd_end:
        s = lines[i].strip()
        if s.startswith('elif cmd') or s.startswith('elif _lower'):
            break
        new_cmd_lines.append(lines[i])
        i += 1

    # Add dispatch_auto call (before the elif chain)
    new_cmd_lines.append('    # Auto-eligible commands (from commands.py registry)\n')
    new_cmd_lines.append('    if _commands_dispatch(cmd, role, name, badge, globals()):\n')
    new_cmd_lines.append('        return True\n')
    new_cmd_lines.append('\n')

    # Process elif blocks
    removed = 0
    kept = 0
    while i < cmd_end:
        s = lines[i].strip()

        if s.startswith('elif cmd') or s.startswith('elif _lower'):
            block_keys = extract_keys_from_elif(s)
            is_auto = False
            if block_keys:
                for bk in block_keys:
                    if bk in auto_keys:
                        is_auto = True
                        break

            if is_auto:
                block_end = skip_block(lines, i, cmd_end)
                removed += 1
                i = block_end
                continue
            else:
                block_end = skip_block(lines, i, cmd_end)
                new_cmd_lines.extend(lines[i:block_end])
                kept += 1
                i = block_end
                continue

        new_cmd_lines.append(lines[i])
        i += 1

    # Reconstruct: everything before handle_cmd + new handle_cmd + everything after
    output = lines[:cmd_start] + new_cmd_lines + lines[cmd_end:]

    with open(AI_PY, 'w', encoding='utf-8') as f:
        f.writelines(output)

    new_total = len(output)
    print(f"  Removed: {removed} auto-eligible elif blocks")
    print(f"  Kept: {kept} manual elif blocks")
    print(f"  Original file: {len(lines)} lines")
    print(f"  New file: {new_total} lines")
    print(f"  Lines saved: {len(lines) - new_total}")


def extract_keys_from_elif(s):
    keys = []
    m = re.match(r'elif cmd == "(.+)"', s)
    if m:
        return [m.group(1)]
    m = re.match(r'elif cmd in \((.+)\)', s)
    if m:
        return re.findall(r'"([^"]*)"', m.group(1))
    m = re.match(r"elif cmd.startswith\(['\"](.+?)['\"]\)", s)
    if m:
        return ['__prefix:' + m.group(1)]
    m = re.match(r'elif cmd\.split\(" ", 1\)\[0\] in \((.+)\)', s)
    if m:
        return ['__split0:' + k for k in re.findall(r'"([^"]*)"', m.group(1))]
    m = re.match(r'elif _lower == "(.+)"', s)
    if m:
        return [m.group(1)]
    m = re.match(r'elif _lower in \((.+)\)', s)
    if m:
        return re.findall(r'"([^"]*)"', m.group(1))
    m = re.match(r"elif _lower.startswith\(['\"](.+?)['\"]\)", s)
    if m:
        return ['__prefix:' + m.group(1)]
    return None


def skip_block(lines, start, limit):
    i = start + 1
    base_indent = len(lines[start]) - len(lines[start].lstrip())
    while i < limit:
        s = lines[i].rstrip()
        s_stripped = s.strip()
        if not s_stripped:
            i += 1
            continue
        j_indent = len(s) - len(s.lstrip())
        if j_indent <= base_indent and s_stripped:
            if s_stripped.startswith('elif ') or s_stripped.startswith('else:') or s_stripped.startswith('def '):
                return i
        i += 1
    return limit


if __name__ == '__main__':
    main()
