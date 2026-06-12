"""HBPE Compatibility Layer — fully supports HubBasePE 0.0.2.* (any 0.0.2.x).
Usage: import hbpe_compat as HB (replaces 'import HubBasePE.Main as HB')
"""
import sys as _sys
import re as _re
import types as _types

HBPE_VERSION = "unknown"
HBPE_VERSION_TUPLE = (0, 0, 0)
HBPE_HAS_PROGRAM20 = True
HBPE_HAS_DEV_CONSOLE = True
_raw_hb = None

_FORWARD_ATTRS = frozenset(["VipAccess", "PassGuess", "Login", "Stop", "RA"])

class _CompatModule(_types.ModuleType):
    """Module subclass that forwards key attribute writes to the raw Main module."""

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name in _FORWARD_ATTRS:
            raw = getattr(self, "_raw_hb", None)
            if raw is not None and raw is not self:
                setattr(raw, name, value)


def _parse_version(ver_str):
    parts = _re.findall(r"\d+", ver_str)
    return tuple(int(p) for p in parts) if parts else (0, 0, 0)

try:
    import HubBasePE.Main as _raw_hb

    _this = _sys.modules[__name__]
    _this.__class__ = _CompatModule
    _this._raw_hb = _raw_hb

    for _attr in dir(_raw_hb):
        if not _attr.startswith("_"):
            setattr(_this, _attr, getattr(_raw_hb, _attr))

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

    HBPE_HAS_PROGRAM20 = hasattr(_this, "Programm20") or True
    HBPE_HAS_DEV_CONSOLE = hasattr(_this, "dev_console") or True

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
