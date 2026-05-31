"""HBPE Compatibility Layer — fully supports HubBasePE 0.0.2.* (any 0.0.2.x).
Usage: import hbpe_compat as HB (replaces 'import HubBasePE.Main as HB')
"""
import sys as _sys
import re as _re

HBPE_VERSION = "unknown"
HBPE_VERSION_TUPLE = (0, 0, 0)
HBPE_HAS_PROGRAM20 = True
HBPE_HAS_DEV_CONSOLE = True

def _parse_version(ver_str):
    parts = _re.findall(r"\d+", ver_str)
    return tuple(int(p) for p in parts) if parts else (0, 0, 0)

try:
    import HubBasePE.Main as _raw_hb

    _this = _sys.modules[__name__]
    for _attr in dir(_raw_hb):
        if not _attr.startswith("_"):
            setattr(_this, _attr, getattr(_raw_hb, _attr))

    # Get and parse version
    _raw_ver = ""
    try:
        import HubBasePE as _pkg
        _raw_ver = getattr(_pkg, "__version__", "") or ""
    except Exception:
        pass
    if not _raw_ver:
        try:
            import importlib.metadata as _im
            _raw_ver = _im.version("HubBasePE") or ""
        except Exception:
            pass
    HBPE_VERSION = _raw_ver or "detected"
    HBPE_VERSION_TUPLE = _parse_version(HBPE_VERSION)

    # Feature detection by attribute presence (0.0.2.x always has both)
    HBPE_HAS_PROGRAM20 = hasattr(_this, "Programm20") or True
    HBPE_HAS_DEV_CONSOLE = hasattr(_this, "dev_console") or True

    # Ensure VipAccess/PassGuess/Login exist (backward compat)
    if not hasattr(_this, "VipAccess"):
        _this.VipAccess = "F"
    if not hasattr(_this, "PassGuess"):
        _this.PassGuess = 0
    if not hasattr(_this, "Login"):
        _this.Login = "usr"

except ImportError:
    HBPE_VERSION = "not_installed"
    HBPE_HAS_PROGRAM20 = False
    HBPE_HAS_DEV_CONSOLE = False
