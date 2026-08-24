"""HBPE Compatibility Layer - supports HubBasePE 0.0.2.x:
old globals-based API (<= 0.0.2.0.0.5), list-based API (0.0.2.0.1 - 0.0.2.0.10,
Code/Restart take prList) and the User-based API (>= 0.0.2.0.11,
Code/Restart take (prList, User)). Also previews the 0.0.3+ HubBase_rewrite
(Session/Program architecture, filesystem-discovered programs).
0.0.2.x is LTS upstream: "auto" keeps it primary until at least 0.0.3.0.00
final; the rewrite stays opt-in behind AI_HBPE_MODE=rewrite.
Mode selection via environment variable AI_HBPE_MODE (set before import):
  - "auto" (default): HubBasePE 0.0.2.x first, then HubBase_rewrite preview
  - "list":           HubBasePE 0.0.2.x only
  - "rewrite":        HubBase_rewrite only (needs Python >= 3.12 and the
                      folder named HubBase_rewrite importable on sys.path)
The rewrite bridge synthesizes a silent Session (never prompts, never
registers), discovers programs from disk, exposes lazy Programm<id>
callables plus an interactive picker shim for Code()/Start()/Restart().
Callers always use arg-less forms; the layer shields callers from upstream
sys.exit() calls.
Usage: import hbpe_compat as HB (replaces 'import HubBasePE.Main as HB')
"""
import os as _os
import sys as _sys
import re as _re
import types as _types
from types import SimpleNamespace as _SimpleNamespace

_mode = (_os.environ.get("AI_HBPE_MODE") or "auto").strip().lower()
if _mode not in ("auto", "list", "rewrite"):
    _mode = "auto"
HBPE_MODE = _mode

HBPE_VERSION = "unknown"
HBPE_VERSION_TUPLE = (0, 0, 0)
HBPE_HAS_PROGRAM20 = False
HBPE_HAS_PROGRAM21 = False
HBPE_HAS_DEV_CONSOLE = False
HBPE_API = "none"
HBPE_MODULES = {}
_raw_hb = None
_raw_rw = None
_prList = {}
_pprList = {}
_user = None
_rw_session = None

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


def _noop(*_args, **_kwargs):
    return None


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
    import inspect as _inspect

    def _param_count(fn):
        try:
            return len(_inspect.signature(fn).parameters)
        except (TypeError, ValueError):
            return 1

    _imp_errs = []

    if _mode in ("auto", "list"):
        try:
            import HubBasePE.Main as _raw_hb
        except ImportError as _e:
            _imp_errs.append(_e)

    if _raw_hb is None and _mode in ("auto", "rewrite"):
        try:
            # The rewrite mixes two import roots: 'HubBase_rewrite.*' needs
            # its parent on sys.path, while main.py's bare 'import Programs'
            # needs the package dir itself. Prepare both before importing.
            import HubBase_rewrite as _rw_pkg
            try:
                _rw_dir = list(_rw_pkg.__path__)[0]
                if _rw_dir not in _sys.path:
                    _sys.path.insert(0, _rw_dir)
            except Exception:
                pass
            import HubBase_rewrite.main as _raw_rw
        except (ImportError, SyntaxError) as _e:
            _imp_errs.append(_e)

    _this = _sys.modules[__name__]
    _this.__class__ = _CompatModule

    if _raw_hb is not None:
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
        HBPE_HAS_PROGRAM21 = hasattr(_raw_hb, "Programm21")
        HBPE_HAS_DEV_CONSOLE = hasattr(_raw_hb, "dev_console")

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

    elif _raw_rw is not None:
        # 0.0.3+ HubBase_rewrite bridge (Session/Program architecture).
        HBPE_API = "rewrite"
        HBPE_VERSION = getattr(_raw_rw, "__version__", "") or "0.0.3"
        HBPE_VERSION_TUPLE = _parse_version(HBPE_VERSION)

        _rw_programs = []
        _RWSession = None
        _RWProgram = None
        _RWUser = None
        try:
            from Programs import all_programs as _rw_all
            _rw_programs = [str(_p) for _p in _rw_all]
            from Programs.Manager import Session as _S, Program as _P
            _RWSession, _RWProgram = _S, _P
            from HubBase_rewrite.Database import User as _U
            _RWUser = _U
        except Exception:
            _rw_programs = []
            _RWSession = _RWSession or None
            _RWProgram = _RWProgram or None

        def _ensure_session():
            """Silent Session: never prompts, never registers."""
            global _rw_session
            if _RWSession is None:
                return None
            if _rw_session is None:
                _rw_session = _RWSession()
                _rw_session.logged_in = True
            return _rw_session

        def _run_id(pid):
            sess = _ensure_session()
            if sess is None:
                print("Rewrite engine unavailable (Programs.Manager import failed).")
                return False
            try:
                _ok, _meta = _RWProgram(str(pid)).run(sess)
                return bool(_ok)
            except SystemExit:
                return None

        for _pid in sorted(set(_rw_programs)):
            if _pid.isdigit():
                setattr(_this, "Programm{}".format(int(_pid)),
                        (lambda _p: lambda *_a, **_k: _run_id(_p))(_pid))

        _prList = {int(_p): (lambda q: lambda *_a, **_k: _run_id(q))(_p)
                   for _p in _rw_programs if str(_p).isdigit()}
        _pprList = {}

        HBPE_HAS_PROGRAM20 = "20" in _rw_programs
        HBPE_HAS_PROGRAM21 = False
        HBPE_HAS_DEV_CONSOLE = False

        def _picker():
            """Interactive program chooser standing in for upstream's future menu."""
            print("=== HubBase v{} (preview bridge) ===".format(HBPE_VERSION))
            while True:
                print("Available programs: {}".format(", ".join(_rw_programs) or "(none discovered)"))
                _choice = input("Program number or q -- ").strip()
                if _choice.lower() in ("q", "n", "quit", "exit"):
                    return None
                _cid = _choice[1:] if _choice[:1].upper() == "P" else _choice
                if _cid.isdigit() and _cid in _rw_programs:
                    _run_id(_cid)
                elif _choice:
                    print("Unknown program.")

        def Start(pprList=None):
            """Preview alias: opens the interactive program picker."""
            try:
                return _picker()
            except SystemExit:
                return None

        def Code(prList=None):
            """Preview alias: opens the interactive program picker."""
            try:
                return _picker()
            except SystemExit:
                return None

        def Restart(prList=None):
            """Preview alias: reopens the interactive program picker."""
            try:
                return _picker()
            except SystemExit:
                return None

        def Advance(*_args, **_kwargs):
            """Legacy no-op."""
            return None

        def PStop(*_args, **_kwargs):
            """Legacy no-op."""
            return None

        def current_user():
            """Session user if a real rewrite User is attached, else None."""
            _sess = _ensure_session()
            _u = getattr(_sess, "user", None)
            return _u if (_RWUser is not None and isinstance(_u, _RWUser)) else None

        def set_vip(state):
            """Map VIP state onto the session's rewrite User when present."""
            _st = bool(state)
            _sess = _ensure_session()
            _u = getattr(_sess, "user", None)
            if _u is not None and _RWUser is not None and isinstance(_u, _RWUser):
                _u.VipAccess = _st
            _this.VipAccess = "T" if _st else "F"

        if not hasattr(_this, "VipAccess"):
            _this.VipAccess = "F"
        if not hasattr(_this, "PassGuess"):
            _this.PassGuess = 0
        if not hasattr(_this, "Login"):
            _this.Login = "usr"

    else:
        HBPE_VERSION = "not_installed"
        _missing = getattr(_imp_errs[0], "name", None) if _imp_errs else None
        _missing = _missing or "; ".join(str(e) for e in _imp_errs) or "no compatible package found"
        _mode_note = ""
        if _mode == "rewrite":
            _mode_note = " (AI_HBPE_MODE=rewrite: HubBase_rewrite requires Python >= 3.12 and its parent folder on sys.path)"
        elif _mode == "list":
            _mode_note = " (AI_HBPE_MODE=list: HubBasePE 0.0.2.x not found)"

        def _unavailable(*_args, **_kwargs):
            raise RuntimeError("HubBasePE unavailable (missing: {}){}".format(_missing, _mode_note))

        for _fname in ("Start", "Code", "Restart", "ProgramCycle", "ProgrammCycle",
                       "Advance", "PStop"):
            setattr(_this, _fname, _unavailable)

except ImportError as _imp_err:
    HBPE_VERSION = "not_installed"
    _missing = getattr(_imp_err, "name", None) or str(_imp_err)

    def _unavailable(*_args, **_kwargs):
        raise RuntimeError("HubBasePE unavailable (missing: {})".format(_missing))

    for _fname in ("Start", "Code", "Restart", "ProgramCycle", "ProgrammCycle",
                   "Advance", "PStop"):
        setattr(_sys.modules[__name__], _fname, _unavailable)
