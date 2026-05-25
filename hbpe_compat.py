"""HBPE Compatibility Layer — supports HubBasePE 0.0.1.2.01 and 0.0.2.0.00b1.
Usage: import hbpe_compat as HB (replaces 'import HubBasePE.Main as HB')
"""
import sys as _sys

HBPE_VERSION = "unknown"
HBPE_HAS_PROGRAM20 = False
HBPE_HAS_DEV_CONSOLE = False

try:
    import HubBasePE.Main as _raw_hb

    # Re-export everything from HubBasePE.Main at this module's namespace
    # so 'import hbpe_compat as HB' works identically to 'import HubBasePE.Main as HB'
    _this = _sys.modules[__name__]
    for _attr in dir(_raw_hb):
        if not _attr.startswith("_"):
            setattr(_this, _attr, getattr(_raw_hb, _attr))

    # Feature detection
    HBPE_HAS_PROGRAM20 = hasattr(_this, "Programm20")
    HBPE_HAS_DEV_CONSOLE = hasattr(_this, "dev_console")

    # Ensure VipAccess/PassGuess/Login exist (0.0.1.2.01 style)
    if not hasattr(_this, "VipAccess"):
        _this.VipAccess = "F"
    if not hasattr(_this, "PassGuess"):
        _this.PassGuess = 0
    if not hasattr(_this, "Login"):
        _this.Login = "usr"

    # Get version string
    try:
        import HubBasePE as _pkg
        raw_ver = getattr(_pkg, "__version__", "")
        HBPE_VERSION = raw_ver or "detected"
    except Exception:
        HBPE_VERSION = "detected"

except ImportError:
    HBPE_VERSION = "not_installed"
