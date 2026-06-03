# Project State — AiScript v0.3.0.post1 / AI.py v6.0.0

## Project Structure
```
root/
  AI.py              — main application (v6.0.0, AiScript v0.3.0.post1 integrated)
  AiScript/          — AiScript interpreter, Kite IDE, archives
    aiscript.py      — AiScript v0.3.0.post1 interpreter (main)
    aiscript_ide.py  — Kite IDE v0.2.1.post1
    kite.cmd         — Launcher for Kite
    aiscript_v*.py   — Version archives (0.0.1 through 0.3.0.post1)
    test_aiscript.ais / test_aiscript_v0.0.2.ais / test_aiscript_extra.ais
  hbpe_compat.py     — HubBasePE compatibility layer
  bin/               — datae/ (extras), datagen/ (generators), datab/ (data_bulk*.py)
  HBPE/              — vendored HubBasePE v0.0.2.0.0.2
  Json/              — runtime config (ai_notes.json, ai_todos.json, updater_config.json)
  Installers/        — iss/ (Inno Setup scripts + output EXEs), AIpy/ (builder sources)
  Website/           — Vercel-deployed site (all .html, Installers/, AiScript/ symlinks)
  docs/
  AGENTS.md          — this file
```

## Version Status
- **AiScript**: **v0.3.0.post1** (current, new features: `not` stmt-level, slicing, try/except/finally; fixes: `not`/`and`/`or` expr keywords, `ai.*` module subscript access)
- **Kite IDE**: **v0.2.1.post1** (unchanged)
- **AI.py**: **v6.0.0** (AiScript integrated, `ais`/`run` commands, `ai.*` module)
- **HubBasePE**: v0.0.2.0.0.2 (vendored in HBPE/)

## Key Changes in v0.3.0 (aiscript.py)
1. **`not` at statement level** — `not`, `True`, `False`, `None` now startable as expression statements
2. **Slicing** — `items[1:3]`, `items[:5]`, `items[::2]`, `items[::-1]`, `items[1:5:2]` (lists and strings). `_Slice` AST node added
3. **try/except/finally** — `try: … except var: … finally: …` (bare except, except with var, finally-only, except+finally). `_Try` AST node added
4. **`_Eval.register_module(name, funcs)`** — allows external code (e.g. AI.py) to register custom modules accessible in AiScript

## Fixes in v0.3.0.post1 (aiscript.py)
1. **`not`/`and`/`or` in expressions** — `_or_expr`, `_and_expr`, `_not_expr` now check `_KW` type instead of `_OP` (keywords are tokenized as `KEYWORD`, not `OPERATOR`)
2. **`ai.*` module subscript access** — `_AiMod` object now supports `__getitem__` (falls back to `getattr`), fixing `ai.__version__` and similar attribute access

## Key Changes in v6.0.0 (AI.py)
0. (AI.py v6.0.0 shipped alongside AiScript v0.3.0; post1 is aiscript-only)
1. **`ais <code>`** — run AiScript one-liner (alias for old `aiscript_run`)
2. **`run <path>`** — run AiScript file (alias for old `aiscript_file`)
3. **`ai.*` module** — AI.py functions are exposed to AiScript as `ai.funcname(...)` (auto-filtered to functions defined in AI.py)
4. **AiScript is now a fixed installer component** (always installed with AI.py, not optional)

## Installers
- **AiScript_Setup_v0.2.1.post1.exe** — standalone (AiScript + optional Kite IDE, .ais file assoc., "Edit in Kite")
- **AI.py_Setup_v6.0.0.exe** — full bundle (Core + AiScript/Kite fixed, HBPE vended/Data Bulk/Data Files optional)
- Built via Inno Setup 6.7.3 (`ISCC.exe` at `C:\Users\Trest\AppData\Local\Temp\opencode\InnoSetup\`)
- Side-by-side: standalone uses `{autopf}\AiScript v0.2.1.post1\`; AI.py bundle uses `{app}\AiScript 0.3.0.post1\`
- Registry: 32-bit `Root: HKCR` writes to WOW6432Node — use `Root: HKLM64; Subkey: Software\Classes\...` for 64-bit Explorer

## Verified Features
Hello World, if/elif/else, for loops, while loops, lists (index/append/pop/len), dicts (key access/len), functions (def/return/recursion), closures, classes (init/methods/self), enumerate, isinstance, dict.get, items, insert/remove/sort/reverse, clear, lower/find/startswith/endswith, json.loads/load/dump/dumps, all augmented assignments (+= -= *= /=), del on subscripts, key-evaluation-once for augmented subscripts, **not** expression statements, **slicing** (all forms), **try/except/finally** (all combos)

## AiScript Known Limitations (not fixed)
- No lambdas or anonymous functions
- No list/dict comprehensions
- No class inheritance (parsed but ignored)
- No user `.ais` module imports
- Integer division floors (like Python 2)

## Python Environment
- Python 3.14 (core) in `.venv\`
- `python.exe` at `C:\Users\Trest\AppData\Local\Python\pythoncore-3.14-64\python.exe`
- AVOID `C:\Users\Trest\AppData\Local\Programs\Python\python.exe` (Python 3.5)
- Vercel deploys from `Website/` directory
- Git branch `test` is active dev branch; `master` auto-deploys to Vercel
- Do NOT commit/push unless asked
