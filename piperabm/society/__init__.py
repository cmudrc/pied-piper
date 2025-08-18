from .society import Society

# Bootstraping for DecisionMaking
# Source: https://github.com/aslan-ng/python-bootstrapper
import os, sys, inspect, importlib.util

# 1) import the “official” DecisionMaking
from .decision_making import DecisionMaking as _BaseDecisionMaking


def _discover_local(plugin_name: str):
    # find the folder containing the user's entry-point script
    main_mod = sys.modules.get("__main__")
    if hasattr(main_mod, "__file__"):
        script_dir = os.path.dirname(os.path.abspath(main_mod.__file__))
    else:
        script_dir = os.getcwd()

    # look for a file named decision_making.py next to it
    plugin_path = os.path.join(script_dir, f"{plugin_name}.py")
    if not os.path.isfile(plugin_path):
        return _BaseDecisionMaking

    # dynamically load it as a module
    spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # find any class in that module that subclasses our base
    for obj in vars(mod).values():
        if (
            inspect.isclass(obj)
            and issubclass(obj, _BaseDecisionMaking)
            and obj is not _BaseDecisionMaking
        ):
            return obj

    # fallback if nothing suitable was found
    return _BaseDecisionMaking


# 2) override the name in our package
DecisionMaking = _discover_local("decision_making")
