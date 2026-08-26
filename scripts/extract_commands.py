#!/usr/bin/env python3
"""extract_commands.py - Parse AI.py elif chain and generate command registry.

Reads AI.py, extracts every `elif cmd == / elif cmd in / elif cmd.startswith` branch,
classifies the pattern, and outputs a JSON registry mapping command names to handler specs.

Output: scripts/commands_registry.json
"""
import re
import json
import sys
import os

AI_PY = os.path.join(os.path.dirname(__file__), '..', 'AI.py')

def parse_cmd_keys(line):
    """Extract command key strings from an elif cmd line."""
    s = line.strip()
    keys = []
    # elif cmd == "value"
    m = re.match(r'elif cmd == "(.+)"', s)
    if m:
        return [m.group(1)]
    # elif cmd in ("v1","v2",...) or elif cmd in ("v1","v2")
    m = re.match(r'elif cmd in \((.+)\)', s)
    if m:
        inner = m.group(1)
        keys = re.findall(r'"([^"]*)"', inner)
        return keys
    # elif cmd.startswith('prefix')
    m = re.match(r"elif cmd.startswith\(['\"](.+?)['\"]\)", s)
    if m:
        return ['__prefix:' + m.group(1)]
    # elif cmd.split(" ", 1)[0] in ("v1","v2",...)
    m = re.match(r'elif cmd\.split\(" ", 1\)\[0\] in \((.+)\)', s)
    if m:
        inner = m.group(1)
        keys = re.findall(r'"([^"]*)"', inner)
        return ['__split0:' + k for k in keys]
    return None


def classify_body(lines, start_idx):
    """Classify the body of a command branch starting at start_idx.
    Returns (pattern_type, detail_dict)."""
    body_lines = []
    i = start_idx
    while i < len(lines):
        s = lines[i].strip()
        # Stop at next top-level elif/if/else at same indent
        if i > start_idx and (s.startswith('elif ') or s.startswith('else:') or s.startswith('def ') or s.startswith('class ')):
            break
        body_lines.append(lines[i])
        i += 1

    if not body_lines:
        return 'empty', {}

    first = body_lines[0].strip()

    # Pattern: try: ... except (most common)
    if first == 'try:':
        try_body_lines = []
        j = 1
        while j < len(body_lines):
            s = body_lines[j].strip()
            if s.startswith('except'):
                break
            try_body_lines.append(body_lines[j])
            j += 1
        try_first = try_body_lines[0].strip() if try_body_lines else ''

        # try: print(func())
        if len(try_body_lines) == 1 and try_first.startswith('print('):
            fn = extract_print_func(try_first)
            if fn:
                return 'try_print', {'fn': fn}

        # try: _d = func(); print preview
        if try_first.startswith('_d = ') or try_first.startswith('_data = '):
            fn_match = re.search(r'=\s*(\w+)\(\)', try_first)
            if fn_match:
                return 'data_preview', {'fn': fn_match.group(1)}

        # try: print(func()) with more lines
        if try_first.startswith('print('):
            fn = extract_print_func(try_first)
            if fn:
                return 'try_print', {'fn': fn}

        # try: assignment = func() (various patterns)
        if '=' in try_first and '(' in try_first:
            # Check if it's a simple assignment
            assign_match = re.match(r'(\w+)\s*=\s*(\w+)\(\)', try_first)
            if assign_match:
                return 'try_assign', {'var': assign_match.group(1), 'fn': assign_match.group(2)}

        # try: n = int(input(...)) - interactive
        if 'input(' in try_first:
            return 'input_interactive', {'code': try_first}

        # try: complex multi-line
        return 'try_complex', {'lines': [l.rstrip() for l in try_body_lines[:5]]}

    # Pattern: print(func()) directly (no try)
    if first.startswith('print('):
        fn = extract_print_func(first)
        if fn:
            return 'direct_print', {'fn': fn}
        # print with format/args
        return 'direct_print_format', {'line': first}

    # Pattern: inline with semicolons
    if ';' in first and first.startswith('print('):
        return 'inline_print', {'line': first}

    # Pattern: if/else block
    if first.startswith('if '):
        return 'if_else', {'lines': [l.rstrip() for l in body_lines[:6]]}

    # Pattern: input-based (no try wrapper)
    if 'input(' in first:
        return 'input_interactive', {'code': first}

    # Pattern: variable assignment
    if '=' in first and not first.startswith('print'):
        return 'assignment', {'line': first}

    # Pattern: function call without print
    if '(' in first and not first.startswith('print'):
        return 'direct_call', {'line': first}

    return 'other', {'lines': [l.rstrip() for l in body_lines[:5]]}


def extract_print_func(line):
    """Extract function name from print(func()) or print(func()) pattern."""
    m = re.match(r'print\((\w+)\(\)\)', line.strip())
    if m:
        return m.group(1)
    # print(func()) with trailing stuff
    m = re.match(r'print\((\w+)\(\),', line.strip())
    if m:
        return m.group(1)
    return None


def main():
    with open(AI_PY, encoding='utf-8') as f:
        lines = f.readlines()

    # Find handle_cmd function
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def handle_cmd('):
            start = i
            break

    if start is None:
        print("ERROR: handle_cmd not found", file=sys.stderr)
        sys.exit(1)

    registry = {}
    special = []  # commands that need manual handling
    stats = {}

    i = start + 1
    while i < len(lines):
        s = lines[i].strip()

        # Stop at next top-level def
        if s.startswith('def ') and not s.startswith('def handle_cmd'):
            break

        # Parse elif cmd lines
        if s.startswith('elif cmd ==') or s.startswith('elif cmd in') or s.startswith('elif cmd.startswith') or s.startswith('elif cmd.split'):
            keys = parse_cmd_keys(s)
            if keys is None:
                i += 1
                continue

            pattern, detail = classify_body(lines, i + 1)
            stats[pattern] = stats.get(pattern, 0) + 1

            for key in keys:
                entry = {'pattern': pattern}
                entry.update(detail)

                # Check if this has role requirement
                if 'and role ==' in s:
                    role_match = re.search(r'and role == "(\w+)"', s)
                    if role_match:
                        entry['role'] = role_match.group(1)

                registry[key] = entry

        i += 1

    # Output
    print(f"Total commands extracted: {len(registry)}")
    print(f"\nPattern breakdown:")
    for p, c in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {p:30s} {c:5d}")

    out_path = os.path.join(os.path.dirname(__file__), 'commands_registry.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    print(f"\nRegistry written to: {out_path}")

    # Also output a summary of 'other' and 'input_interactive' commands for manual review
    manual = {k: v for k, v in registry.items()
              if v['pattern'] in ('input_interactive', 'if_else', 'other', 'assignment', 'direct_call', 'inline_print', 'direct_print_format')}
    manual_path = os.path.join(os.path.dirname(__file__), 'commands_manual_review.json')
    with open(manual_path, 'w', encoding='utf-8') as f:
        json.dump(manual, f, indent=2, ensure_ascii=False)
    print(f"Manual review needed: {len(manual)} commands -> {manual_path}")


if __name__ == '__main__':
    main()
