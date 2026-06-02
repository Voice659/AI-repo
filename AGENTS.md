# Project State — AiScript v0.2.1 / AI.py v5.5.1

## Project Structure
```
root/
  AI.py              — main application (v5.5.1, Introducing AiScript)
  AiScript/          — AiScript interpreter, Kite IDE, archives
    aiscript.py      — AiScript v0.2.1 interpreter (main)
    aiscript_ide.py  — Kite IDE v0.2.1
    kite.cmd         — Launcher for Kite
    aiscript_v*.py   — Version archives (0.0.1 through 0.2.1)
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
- **AiScript**: **v0.2.1** (current, 18 critical fixes applied)
- **Kite IDE**: **v0.2.1** (same version, bundled with AiScript)
- **AI.py**: **v5.5.1** (Introducing AiScript)
- **HubBasePE**: v0.0.2.0.0.2 (vendored in HBPE/)

## AiScript v0.2.1 — All Fixes Applied
### aiscript.py (10 fixes)
1. `del` operator walks scope chain to find variable
2. `json.dump`/`json.load`/`_builtin_open` — proper context-manager close (no fd leak)
3. `int()` no-op branch collapsed to avoid unexpected behavior
4. REPL Ctrl+C raises `KeyboardInterrupt` (not bare `except:`)
5. `run_file` wraps traceback cleanly without raw frame dump
6. CLI sets `sys.ais_argv` instead of leaving it empty
7. `_StopSignal` exception + `_stop_flag` check for forced script halt
8. `except EOFError: break` in REPL for non-interactive / piped input
9. REPL banner uses ASCII hyphen `--` instead of em dash `—` (cp866 fix)
10. **Augmented assignment double-evaluation** — subscript keys evaluated once via `_apply_aug_op`

### aiscript_ide.py (8 fixes)
1. Debounced syntax highlight on keystroke (200ms timer)
2. Unsaved-changes confirmation dialog on Open
3. Word-count caching in `_on_key` (avoids full re-highlight)
4. Dynamic line-number width from digit count (not hardcoded)
5. Font-metrics-based line height (not hardcoded 20px)
6. Stop button with `threading.Event` stop flag
7. `except SystemExit:` catch for clean exit
8. Console output trimmed at 500 lines

## Installers
- **AiScript_Setup_v0.2.1.exe** — standalone (AiScript + optional Kite IDE, .ais file assoc., "Edit in Kite")
- **AI.py_Setup_v5.5.0.exe** — full bundle (Core + optional AiScript/Kite/HBPE vended/Data Bulk 1-31/Data Files)
- Built via Inno Setup 6.7.3 (`ISCC.exe` at `C:\Users\Trest\AppData\Local\Temp\opencode\InnoSetup\`)
- Side-by-side: standalone uses `{autopf}\AiScript v0.2.1\`; AI.py bundle uses `{app}\AiScript 0.2.1\`
- Registry: 32-bit `Root: HKCR` writes to WOW6432Node — use `Root: HKLM64; Subkey: Software\Classes\...` for 64-bit Explorer

## Verified Features (test_aiscript.ais + test_aiscript_extra.ais — all pass)
Hello World, if/elif/else, for loops, while loops, lists (index/append/pop/len), dicts (key access/len), functions (def/return/recursion), closures, classes (init/methods/self), enumerate, isinstance, dict.get, items, insert/remove/sort/reverse, clear, lower/find/startswith/endswith, json.loads/load/dump/dumps, all augmented assignments (+= -= *= /=), del on subscripts, key-evaluation-once for augmented subscripts

## AiScript Known Limitations (not fixed)
- No try/except/finally
- No lambdas or anonymous functions
- No list/dict comprehensions
- No slicing (`items[1:3]`)
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
