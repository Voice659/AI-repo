"""HBPE Compatibility Layer - supports HubBasePE 0.0.2.x:
old globals-based API (<= 0.0.2.0.0.5), list-based API (0.0.2.0.1 - 0.0.2.0.10,
Code/Restart take prList) and the User-based API (>= 0.0.2.0.11,
Code/Restart take (prList, User)). Callers always use arg-less forms;
the layer auto-detects signatures, synthesizes a silent User when needed
and shields callers from upstream sys.exit() calls.
Usage: import hbpe_compat as HB (replaces 'import HubBasePE.Main as HB')
"""
import sys as _sys
import re as _re
import types as _types
from types import SimpleNamespace as _SimpleNamespace

HBPE_VERSION = "unknown"
HBPE_VERSION_TUPLE = (0, 0, 0)
HBPE_HAS_PROGRAM20 = False
HBPE_HAS_DEV_CONSOLE = False
HBPE_API = "none"
HBPE_MODULES = {}
_raw_hb = None
_prList = {}
_pprList = {}
_user = None

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


def _make_user():
    """Return a cached User-compatible object without any prompts."""
    global _user
    if _user is None:
        cls = getattr(_raw_hb, "User", None)
        if cls is not None:
            try:
                _user = cls("usr")
            except Exception:
                _user = None
        if _user is None:
            _user = _SimpleNamespace(VipAccess=False, username="usr", log_in=lambda: None)
    _user.VipAccess = bool(getattr(_raw_hb, "VipAccess", False))
    return _user


def current_user():
    """Public accessor for the synthesized User object."""
    if _raw_hb is None:
        return None
    return _make_user()


def set_vip(state):
    """Set VIP state consistently across raw module, cached user and this layer."""
    st = bool(state)
    if _raw_hb is not None:
        setattr(_raw_hb, "VipAccess", st)
    u = _make_user()
    u.VipAccess = st
    VipAccess = st


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

    def _param_count(fn):
        try:
            return len(_inspect.signature(fn).parameters)
        except (TypeError, ValueError):
            return 1

    try:
        _code_params = _param_count(_raw_hb.Code)
    except Exception:
        _code_params = 0

    if _code_params > 0:
        # List-based API (0.0.2.0.1+): functions require prList.
        HBPE_API = "list"
        try:
            _lists = _raw_hb.Setup_HubBase()
            _prList = _lists[0] if isinstance(_lists[0], dict) else {}
            _second = _lists[1] if len(_lists) > 1 else {}
            if isinstance(_second, dict):
                if _second and all(isinstance(k, str) for k in _second.keys()):
                    # Future launcher-style Setup returning (prList, modules).
                    HBPE_MODULES = _second
                    _pprList = getattr(_raw_hb, "pprList", {})
                    if not isinstance(_pprList, dict):
                        _pprList = {}
                else:
                    _pprList = _second
        except Exception:
            _prList, _pprList = {}, {}

        def Start(pprList=None):
            """Start PE with the Plus programs (pprList/User auto-detected)."""
            lst = _pprList if pprList is None else pprList
            if not lst:
                print("No Plus-program list available in HBPE v{}.".format(HBPE_VERSION))
                return None
            args = [lst]
            if _param_count(_raw_hb.Start) >= 2:
                args.append(_make_user())
            try:
                return _raw_hb.Start(*args)
            except SystemExit:
                return None

        def Code(prList=None):
            """Run the PE Code system (prList/User auto-detected)."""
            args = [_prList if prList is None else prList]
            if _param_count(_raw_hb.Code) >= 2:
                args.append(_make_user())
            try:
                return _raw_hb.Code(*args)
            except SystemExit:
                return None

        def Restart(prList=None):
            """Restart the PE program chooser (prList/User auto-detected)."""
            args = [_prList if prList is None else prList]
            if _param_count(_raw_hb.Restart) >= 2:
                args.append(_make_user())
            try:
                return _raw_hb.Restart(*args)
            except SystemExit:
                return None

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

except ImportError as _imp_err:
    HBPE_VERSION = "not_installed"
    HBPE_HAS_PROGRAM20 = False
    HBPE_HAS_DEV_CONSOLE = False
    _missing = getattr(_imp_err, "name", None) or str(_imp_err)

    def _unavailable(*_args, **_kwargs):
        raise RuntimeError("HubBasePE unavailable (missing: {})".format(_missing))

    for _fname in ("Start", "Code", "Restart", "ProgramCycle", "ProgrammCycle",
                   "Advance", "PStop"):
        setattr(_sys.modules[__name__], _fname, _unavailable)
