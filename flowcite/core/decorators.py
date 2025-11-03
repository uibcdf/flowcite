from __future__ import annotations

from functools import wraps
from .collector import track_target


def scoped_usage(target: str):
    """
    Decorator to mark that this target (function/method) was used in the workflow.
    """
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            track_target(target)
            return fn(*args, **kwargs)
        return wrapper
    return deco

