from __future__ import annotations

from .collector import get_used_items
from .registry import Registry
from ..formats import markdown, text, bibtex, jsonfmt


def report(format: str = "markdown") -> str:
    used = get_used_items()
    items = Registry.items

    if format == "markdown":
        return markdown.render(used, items)
    if format == "text":
        return text.render(used, items)
    if format == "bibtex":
        return bibtex.render(used, items)
    if format == "json":
        return jsonfmt.render(used, items)
    # default fallback
    return text.render(used, items)
