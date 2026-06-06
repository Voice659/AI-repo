# Historical Installer Archives

## Standalone AiScript Installers (v0.1.0–v0.1.3)

These Inno Setup EXEs recreate the historical standalone installers. Each bundles:

- **Interpreter**: `aiscript_v0.0.2.py` (the interpreter at that time was identical to v0.0.2 across all v0.1.x versions)
- **Kite IDE** (the matching IDE version for that release)
- `.ais` file association with flat "Edit in Kite" right-click command

### Downloads

| Version | File | IDE Version | What's New |
|---------|------|-------------|------------|
| v0.1.0 | `AiScript_Setup_v0.1.0.exe` | v0.1.0 | First Kite IDE release (tkinter, syntax highlighting, inline runner) |
| v0.1.1 | `AiScript_Setup_v0.1.1.exe` | v0.1.1 | Scroll sync crash fix + thread-safe Tkinter |
| v0.1.2 | `AiScript_Setup_v0.1.2.exe` | v0.1.2 | ctypes console-hide block |
| v0.1.3 | `AiScript_Setup_v0.1.3.exe` | v0.1.3 | `_load_file`/`filepath`/`main()` + rebrand to "Kite" |
| v0.1.4 | `AiScript_Setup_v0.1.4.exe` | v0.1.3 | Initial standalone Inno Setup release |

All EXEs are available in `Website/Installers/` and `AiScript/backups/`.

## Kite IDE Version Lineage

| Version | File | Changes |
|---------|------|---------|
| v0.1.0 | `aiscript_ide_v0.1.0.py` | Original. tkinter GUI, syntax highlighting, inline runner via `aiscript._Eval`. |
| v0.1.1 | `aiscript_ide_v0.1.1.py` | `v_scroll` → `self.v_scroll` (instance var). `_sync_vscroll` calls `self.v_scroll.set()` (no crash). `_execute` uses queue sentinel for thread-safe status update. `_poll_output` handles sentinel tuple. |
| v0.1.2 | `aiscript_ide_v0.1.2.py` | v0.1.1 + ctypes console-hide block. Still "AiScript IDE", no `main()`. |
| v0.1.3 | `aiscript_ide_v0.1.3.py` | v0.1.2 + `_load_file`/`filepath`/`main()`. Rebranded to "Kite". `evaluator.globals.let` print override. |

## kite.cmd Launcher

| Version | File | Contents |
|---------|------|----------|
| v0.1.2 | `kite_v0.1.2.cmd` | `@echo off` `start "" pythonw.exe "%~dp0aiscript_ide.py"` |
| v0.1.3+ | `kite.cmd` | `@echo off` `start "" pythonw.exe "%~dp0aiscript_ide.py" %*` |

## Source Files

- **ISS scripts**: `Installers/iss/archives/aiscript_setup_v0.1.0.iss` through `aiscript_setup_v0.1.3.iss`
- **Compiled EXEs**: `Installers/iss/archives/output/`
- **Website copies**: `Website/Installers/`
- **Backup copies**: `AiScript/backups/`
