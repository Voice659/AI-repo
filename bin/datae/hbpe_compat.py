"""HBPE Compatibility Layer - bridges all HubBasePE eras.

Supported upstream APIs:
  0.0.2.x  globals-based (<= 0.0.2.0.0.5), list-based (0.0.2.0.1+),
           User-based (>= 0.0.2.0.11, Code/Restart take (prList, User)).
  0.0.3+   HubBase main Programs/ architecture (Program.run(), no Session).

Detection order:
  1. Local vendor (HBPE/HubBasePE/Main.py) → old 0.0.2.x list/globals API.
  2. AI_HBPE_REWRITE_PATH env var → HubBase main Programs/ (rewrite-v2).
  3. HubBase_rewrite package → old b1 preview (rewrite-v1, Session-based).

LTS: 0.0.2.1.x is bugfix-only LTS (EOL after any 0.0.3 pre-release).
Scenario C: PE 0.0.3 winds down to P-programs only, eventually absorbed
into HubBase main (~0.0.3.2 / 0.0.4 / 0.1.0).

Mode selection via environment variable AI_HBPE_MODE (set before import):
  "auto"   (default): old vendor first, then rewrite-v2, then rewrite-v1.
  "list":             old vendor only.
  "rewrite":          rewrite-v2 only (needs AI_HBPE_REWRITE_PATH or
                      HubBase_rewrite importable on sys.path).
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
_rewrite_path = _os.environ.get("AI_HBPE_REWRITE_PATH")

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
        _rw_programs = []
        _RWSession = None
        _RWProgram = None
        _RWUser = None
        _rw_v2 = False

        if _rewrite_path:
            _rewrite_path = _os.path.abspath(_rewrite_path)
            if _os.path.isdir(_rewrite_path):
                try:
                    import importlib.util as _ilu

                    _mgr_file = _os.path.join(_rewrite_path, "Programs", "Manager.py")
                    if _os.path.isfile(_mgr_file):
                        _mgr_spec = _ilu.spec_from_file_location("_hb_rw_manager", _mgr_file)
                        _mgr_mod = _ilu.module_from_spec(_mgr_spec)
                        _sys.modules["_hb_rw_manager"] = _mgr_mod
                        _mgr_spec.loader.exec_module(_mgr_mod)
                        _RWProgram = _mgr_mod.Program

                    _prog_dir = _os.path.join(_rewrite_path, "Programs")
                    if _os.path.isdir(_prog_dir):
                        for _entry in _os.listdir(_prog_dir):
                            _mp = _os.path.join(_prog_dir, _entry, "main.py")
                            if _os.path.isfile(_mp) and _entry.isdigit():
                                _rw_programs.append(_entry)

                    _raw_rw = _types.ModuleType("_hb_rw_v2")
                    _raw_rw.__version__ = "0.0.3"
                    _ver_file = _os.path.join(_rewrite_path, "Data", "versions.json")
                    if _os.path.isfile(_ver_file):
                        try:
                            import json as _json
                            with open(_ver_file, "r", encoding="utf-8") as _vf:
                                _vd = _json.load(_vf)
                            _raw_rw.__version__ = max(_vd.keys())
                        except Exception:
                            pass
                    _sys.modules["_hb_rw_v2"] = _raw_rw

                    _rw_v2 = True
                    HBPE_API = "rewrite"
                except Exception as _e:
                    _imp_errs.append(_e)
                    _rewrite_path = None

        if _raw_rw is None:
            try:
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
            HBPE_API = "list"
            try:
                _lists = _raw_hb.Setup_HubBase()
                _prList = _lists[0] if isinstance(_lists[0], dict) else {}
                _second = _lists[1] if len(_lists) > 1 else {}
                if isinstance(_second, dict):
                    if _second and all(isinstance(k, str) for k in _second.keys()):
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
        HBPE_API = "rewrite"
        HBPE_VERSION = getattr(_raw_rw, "__version__", "") or "0.0.3"
        HBPE_VERSION_TUPLE = _parse_version(HBPE_VERSION)

        if not _rw_v2:
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

        _rw_programs_sorted = sorted(set(_rw_programs))

        if _rw_v2:
            def _run_id(pid):
                if _RWProgram is None:
                    print("Rewrite-v2 engine unavailable (Programs.Manager import failed).")
                    return False
                try:
                    _ok, _meta = _RWProgram(str(pid)).run()
                    return bool(_ok)
                except SystemExit:
                    return None

            def current_user():
                return None

            def set_vip(state):
                _this.VipAccess = "T" if state else "F"

        else:
            def _ensure_session():
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

            def current_user():
                _sess = _ensure_session()
                _u = getattr(_sess, "user", None)
                return _u if (_RWUser is not None and isinstance(_u, _RWUser)) else None

            def set_vip(state):
                _st = bool(state)
                _sess = _ensure_session()
                _u = getattr(_sess, "user", None)
                if _u is not None and _RWUser is not None and isinstance(_u, _RWUser):
                    _u.VipAccess = _st
                _this.VipAccess = "T" if _st else "F"

        for _pid in _rw_programs_sorted:
            if _pid.isdigit():
                setattr(_this, "Programm{}".format(int(_pid)),
                        (lambda _p: lambda *_a, **_k: _run_id(_p))(_pid))

        _prList = {int(_p): (lambda q: lambda *_a, **_k: _run_id(q))(_p)
                   for _p in _rw_programs_sorted if _p.isdigit()}
        _pprList = {}

        HBPE_HAS_PROGRAM20 = "20" in _rw_programs_sorted
        HBPE_HAS_PROGRAM21 = "21" in _rw_programs_sorted
        HBPE_HAS_DEV_CONSOLE = False

        def _picker():
            print("=== HubBase v{} (rewrite bridge) ===".format(HBPE_VERSION))
            while True:
                print("Available programs: {}".format(", ".join(_rw_programs_sorted) or "(none discovered)"))
                _choice = input("Program number or q -- ").strip()
                if _choice.lower() in ("q", "n", "quit", "exit"):
                    return None
                _cid = _choice[1:] if _choice[:1].upper() == "P" else _choice
                if _cid.isdigit() and _cid in _rw_programs_sorted:
                    _run_id(_cid)
                elif _choice:
                    print("Unknown program.")

        def Start(pprList=None):
            """Rewrite alias: opens the interactive program picker."""
            try:
                return _picker()
            except SystemExit:
                return None

        def Code(prList=None):
            """Rewrite alias: opens the interactive program picker."""
            try:
                return _picker()
            except SystemExit:
                return None

        def Restart(prList=None):
            """Rewrite alias: reopens the interactive program picker."""
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
            _mode_note = " (AI_HBPE_MODE=rewrite: set AI_HBPE_REWRITE_PATH or install HubBasePE 0.0.2.x)"
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
