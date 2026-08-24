"""HBPE Compatibility Layer - supports HubBasePE 0.0.2.x:
old globals-based API (<= 0.0.2.0.0.5) and new list-based API (>= 0.0.2.0.1,
where Setup_HubBase() returns (prList, pprList) and Code/Restart/Start take the list).
Usage: import hbpe_compat as HB (replaces 'import HubBasePE.Main as HB')
"""
import sys as _sys
import re as _re
import types as _types

HBPE_VERSION = "unknown"
HBPE_VERSION_TUPLE = (0, 0, 0)
HBPE_HAS_PROGRAM20 = False
HBPE_HAS_DEV_CONSOLE = False
HBPE_API = "none"
_raw_hb = None
_prList = {}
_pprList = {}

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
    if not _raw_ver:
        _raw_ver = getattr(_raw_hb, "__version2__", "") or getattr(_raw_hb, "__version__", "")
    HBPE_VERSION = _raw_ver or "detected"
    HBPE_VERSION_TUPLE = _parse_version(HBPE_VERSION)

    HBPE_HAS_PROGRAM20 = hasattr(_raw_hb, "Programm20")
    HBPE_HAS_DEV_CONSOLE = hasattr(_raw_hb, "dev_console")

    import inspect as _inspect
    try:
        _code_params = len(_inspect.signature(_raw_hb.Code).parameters)
    except (TypeError, ValueError):
        _code_params = 0

    if _code_params > 0:
        # New-style list-based API (0.0.2.0.1+): functions require prList.
        HBPE_API = "list"
        try:
            _lists = _raw_hb.Setup_HubBase()
            _prList, _pprList = _lists[0], _lists[1]
        except Exception:
            _prList, _pprList = {}, {}

        def Start(pprList=None):
            """Start PE with the Plus programs (pprList auto-detected)."""
            return _raw_hb.Start(_pprList if pprList is None else pprList)

        def Code(prList=None):
            """Run the PE Code system (prList auto-detected)."""
            return _raw_hb.Code(_prList if prList is None else prList)

        def Restart(prList=None):
            """Restart the PE program chooser (prList auto-detected)."""
            return _raw_hb.Restart(_prList if prList is None else prList)

    else:
        # Old-style globals-based API (<= 0.0.2.0.0.5): raw callables already copied.
        HBPE_API = "globals"

    if not hasattr(_this, "ProgrammCycle"):
        _pc = getattr(_raw_hb, "ProgramCycle", None) or getattr(_raw_hb, "ProgrammCycle", None)
        if _pc is not None:
            _this.ProgrammCycle = _pc

    if not hasattr(_this, "Advance"):
        def Advance(*_args, **_kwargs):
            """Legacy no-op: upstream removed Advance()/Stop flag."""
            return None
        _this.Advance = Advance

    if not hasattr(_this, "PStop"):
        def PStop(*_args, **_kwargs):
            """Legacy no-op: upstream removed PStop()."""
            return None
        _this.PStop = PStop

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
