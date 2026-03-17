from __future__ import annotations
import atexit
import sys
from importlib.abc import MetaPathFinder
from importlib.util import find_spec
from .collector import get_used_items, track_item
from .registry import Registry

_REMINDER_ENABLED = False

def _exit_reminder():
    """
    Function called at exit to remind the user about collected citations.
    """
    used = get_used_items()
    if not used:
        return

    n_items = len(used)
    msg = (
        f"\n\033[94mℹ️  FlowCite: Your analysis utilized {n_items} components requiring citation.\033[0m\n"
        f"   Run `flowcite.report()` or `flowcite.summary()` to view the full list.\n"
    )
    # Print to stderr to avoid interfering with redirected stdout
    print(msg, file=sys.stderr)

def enable_auto_reminder():
    """
    Enable a polite reminder at the end of the Python session if citations were collected.
    """
    global _REMINDER_ENABLED
    if not _REMINDER_ENABLED:
        atexit.register(_exit_reminder)
        _REMINDER_ENABLED = True

class InjectionsFinder(MetaPathFinder):
    """
    A finder that triggers FlowCite tracking when a registered injection is imported.
    """
    def __init__(self):
        self._triggered = set()

    def find_spec(self, fullname, path, target=None):
        # We don't want to block anything, just trigger if it matches an injection
        if fullname in Registry.injections and fullname not in self._triggered:
            self._triggered.add(fullname)
            item_ids = Registry.injections.get(fullname, [])
            for item_id in item_ids:
                track_item(item_id, used_by=fullname)
        
        # We return None so the normal import process continues
        return None

_IMPORT_HOOKS_ENABLED = False

def enable_import_hooks():
    """
    Enable automatic citation tracking for third-party libraries via import hooks.
    """
    global _IMPORT_HOOKS_ENABLED
    if not _IMPORT_HOOKS_ENABLED:
        sys.meta_path.insert(0, InjectionsFinder())
        _IMPORT_HOOKS_ENABLED = True
