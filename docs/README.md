# Project State — AiScript v0.3.0.post3 / AI.py v6.0.1

## Project Structure
```
root/
  AI.py              — main application (v6.0.1, AiScript v0.3.0.post3 integrated)
  AiScript/          — AiScript interpreter, Kite IDE, archives
    aiscript.py      — AiScript v0.3.0.post3 interpreter (main)
    aiscript_ide.py  — Kite IDE v0.3.0.post3
    kite.cmd         — Launcher for Kite
    aiscript_v*.py   — Version archives (0.0.1 through 0.3.0.post3)
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
- **AiScript**: **v0.3.0.post3** (current, 3 bug fixes: floor-div, import alias, module __getitem__)
- **Kite IDE**: **v0.3.0.post3** (synced to interpreter)
- **AI.py**: **v6.0.1** (inline data extraction data_bulk32-38, import order fix)
- **HubBasePE**: v0.0.2.0.0.2 (vendored in HBPE/)

## Key Changes in v0.3.0 (aiscript.py)
1. **`not` at statement level** — `not`, `True`, `False`, `None` now startable as expression statements
2. **Slicing** — `items[1:3]`, `items[:5]`, `items[::2]`, `items[::-1]`, `items[1:5:2]` (lists and strings). `_Slice` AST node added
3. **try/except/finally** — `try: … except var: … finally: …` (bare except, except with var, finally-only, except+finally). `_Try` AST node added
4. **`_Eval.register_module(name, funcs)`** — allows external code (e.g. AI.py) to register custom modules accessible in AiScript

## Fixes in v0.3.0.post1 (aiscript.py)
1. **`not`/`and`/`or` in expressions** — `_or_expr`, `_and_expr`, `_not_expr` now check `_KW` type instead of `_OP` (keywords are tokenized as `KEYWORD`, not `OPERATOR`)
2. **`ai.*` module subscript access** — `_AiMod` object now supports `__getitem__` (falls back to `getattr`), fixing `ai.__version__` and similar attribute access

## Key Changes in v0.3.0.post2 (aiscript.py)
1. **Versioned "Edit in Kite" cascading submenu** — right-click `.ais` file → "Edit in Kite" → versioned sub-items for each installed Kite. Uses `ExtendedSubCommandsKey` (the Microsoft-documented Win7+ approach) with per-version verbs under `ExtendedSubCommandsKey\Shell\`. Parents use `MUIVerb` + `ExtendedSubCommandsKey` (no `uninsdeletekey`), children use numeric prefix sort order with `uninsdeletekey`. Both `.ais` extension and `AiScriptFile` ProgID get the cascade.
## Fixes in v0.3.0.post2 (installer)
1. **Cascading menu fix** — stale `command` subkey from post1 overrides cascade. ISS files now use `[Code]` with `CurStepChanged(ssInstall)` calling `reg.exe delete ... /reg:64 /f` on the ENTIRE `Edit in Kite` parent key before `[Registry]` runs, ensuring old flat key AND stale `(Default)` value are removed before cascade is created. Replaced `deletekey` + `ValueType: none` (unreliable) with explicit Pascal scripting.
2. **Switched to `ExtendedSubCommandsKey`** — replaced `subcommands = ""` + local `Shell\` subkey (which Windows doesn't recognize for static cascades) with the Microsoft-documented `ExtendedSubCommandsKey` subkey approach (Win7+). Verb display uses `MUIVerb` per Microsoft convention.
3. **Switched to `SubCommands` + `CommandStore`** — `ExtendedSubCommandsKey` doesn't produce cascade under file extensions. Final approach uses `SubCommands` (semicolon-delimited verb list) + `CommandStore\Shell\` for verb implementations. Windows 10/11 flattens cascades with only 1 verb, so added `Windows.properties` as a guaranteed 2nd item.
4. **Both installers list ALL verbs** — the standalone installer's SubCommands now also includes the AI.py verb (`02_Kite_v0.3.0.post2_AIpy`), and AI.py's includes the standalone verb. This ensures reinstalling either installer (in any order) preserves all verbs in the cascade menu. Windows silently skips missing CommandStore entries.

## Fixes in v0.3.0.post3 (aiscript.py)
1. **Floor division bug** — `25-7/8` now returns `24.125` (was `25`; the `/` operator checked `isinstance(l,int) and isinstance(r,int)` and returned `l//r`). Fix: removed the `isinstance` check, always return `l/r` in both `visit_BinOp` and `_eval_assign_augmented`.
2. **Import alias bug** — `import _math` didn't expose a usable module name. Fix: `_import_module` now strips leading underscores via `name.lstrip('_')` before registering the module (`import _math` → `math`).
3. **Module subscript bug** — `_math.add(1,2)` raised `not subscriptable` error. Fix: added `__getitem__` to `_AiScriptModule` class that delegates to `getattr`.

## Key Changes in v6.0.1 (AI.py)
0. (AI.py v6.0.0 shipped alongside AiScript v0.3.0; post1 is aiscript-only)
1. **`ais <code>`** — run AiScript one-liner (alias for old `aiscript_run`)
2. **`run <path>`** — run AiScript file (alias for old `aiscript_file`)
3. **`ai.*` module** — AI.py functions are exposed to AiScript as `ai.funcname(...)` (auto-filtered to functions defined in AI.py)
4. **AiScript is now a fixed installer component** (always installed with AI.py, not optional)

## Installers
- **AiScript_Setup_v0.3.0.post3.exe** — standalone (AiScript + optional Kite IDE, .ais file assoc., versioned "Edit in Kite")
- **AI.py_Setup_v6.0.1.exe** — full bundle v6.0.1 (Core + AiScript v0.3.0.post3 fixed, HBPE vended/Data Bulk/Data Files optional)
- Built via Inno Setup 6.7.3 (`ISCC.exe` at `C:\Users\Trest\AppData\Local\Temp\opencode\InnoSetup\`)
- Side-by-side: standalone uses `{autopf}\AiScript v0.3.0.post3\`; AI.py bundle uses `{app}\AiScript 0.3.0.post3\`
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

## Session Summary — Historical Installer Archives (v0.1.0–v0.1.3)

### Goal
Recreate and compile historical standalone AiScript installer EXEs for all versions between v0.1.0 and v0.1.3, creating matching IDE archives and ensuring the website version history is complete.

### What was done
1. **Created `aiscript_ide_v0.1.1.py`** — v0.1.1 Kite IDE with these fixes over v0.1.0:
   - `_sync_vscroll` crash: changed `self.text.yview(*args)` to `self.v_scroll.set(*args)`
   - `v_scroll` → `self.v_scroll` (instance variable for scroll sync)
   - Thread-safe Tkinter: `_execute` sends `("__update_status__",)` sentinel via queue instead of `self._update_status()` (which became `self.root.after(0, self._update_status)` then final queue approach)
   - `_poll_output` reads `item` (not `text`) and checks for sentinel tuple

2. **Created `aiscript_ide_v0.1.2.py`** — v0.1.2 = v0.1.1 + ctypes console-hide block + version bumped to 0.1.2. Still titled "AiScript IDE v{}", no `main()` function, no `filepath` param yet.

3. **Created `kite_v0.1.2.cmd`** — launcher: `@echo off` `start "" pythonw.exe "%~dp0aiscript_ide.py"`

4. **Created 4 ISS files** in `Installers/iss/archives/` for v0.1.0–v0.1.3:
   - Each bundles interpreter (aiscript_v0.0.2.py as aiscript.py) + matching IDE + optional kite.cmd
   - Flat `Edit in Kite` registry command (no cascading, which came in v0.3.0)
   - `.ais` file association to REPL (python.exe) on double-click
   - REPL uses `/K` flag; IDE uses kite.cmd or direct pythonw.exe

5. **Compiled all 4 installers** with Inno Setup 6.7.3 ISCC.exe

6. **Copied EXEs** to `Website/Installers/` and `AiScript/backups/`

7. **Updated `download.html`** — added 4 rows to the Inno Setup Installer Version History table (v0.1.0–v0.1.3) with descriptions
