"""
FlowCite — trace what you used, cite what matters.
"""

from .core.registry import Registry, register_item, bind, add_injection, load_bibtex, enrich_all
from .core.collector import track_item, track_target, get_used_items, Collector
from .core.decorators import scoped_usage
from .core.report import report, dump
from .core.context import scope
from .contrib.jupyter import summary
from .core.hooks import enable_auto_reminder, enable_import_hooks

enable_persistence = Collector.enable_persistence

__all__ = [
    "Registry",
    "register_item",
    "bind",
    "add_injection",
    "load_bibtex",
    "enrich_all",
    "track_item",
    "track_target",
    "scoped_usage",
    "report",
    "dump",
    "scope",
    "summary",
    "enable_auto_reminder",
    "enable_import_hooks",
    "enable_persistence",
]

