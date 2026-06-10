import sys, types, importlib.util

_HBU_MAIN = None

def _load_hbu():
    global _HBU_MAIN
    if _HBU_MAIN is not None:
        return _HBU_MAIN
    try:
        spec = importlib.util.find_spec("HubBaseUtility.Main")
        if spec is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        # Capture original Showcase to prevent auto-execution
        old_showcase = None
        def _patched_showcase():
            pass
        class _PatchedLoader(spec.loader.__class__):
            def exec_module(self, module):
                super().exec_module(module)
                # Patch out the module-level calls
                if hasattr(module, 'Showcase'):
                    module._original_showcase = module.Showcase
                    module.Showcase = _patched_showcase
        # Use a custom module with patched exec
        spec.loader.exec_module(mod)
        # Restore Showcase
        if hasattr(mod, '_original_showcase'):
            mod.Showcase = mod._original_showcase
            del mod._original_showcase
        sys.modules["HubBaseUtility.Main"] = mod
        _HBU_MAIN = mod
        return mod
    except Exception:
        return None

def get_hbu():
    m = _load_hbu()
    return m

def Showcase():
    m = get_hbu()
    if m:
        m.Showcase()
    else:
        print("HubBaseUtility not installed.")
