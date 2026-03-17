from __future__ import annotations

from pathlib import Path
from .collector import get_used_items
from .registry import Registry
from ..formats import markdown, text, bibtex, jsonfmt, csl_json, provenance


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
    if format == "csl-json" or format == "csl":
        return csl_json.render(used, items)
    if format == "provenance":
        return provenance.render(used, items)
    # default fallback
    return text.render(used, items)


def dump(path: str | Path, formats: list[str] | None = None) -> None:
    """
    Save citation reports in multiple formats to a file or directory.
    If path is a directory, it will save multiple files (e.g., report.md, report.bib).
    If formats is None, it defaults to ["markdown", "bibtex", "provenance"].
    """
    if formats is None:
        formats = ["markdown", "bibtex", "provenance"]
    
    path = Path(path)
    
    # Extensions map
    ext_map = {
        "markdown": "md",
        "bibtex": "bib",
        "json": "json",
        "csl-json": "csl.json",
        "csl": "csl.json",
        "provenance": "txt",
        "text": "txt"
    }

    if path.is_dir() or not path.suffix:
        path.mkdir(parents=True, exist_ok=True)
        for fmt in formats:
            ext = ext_map.get(fmt, "txt")
            filename = f"flowcite_report.{ext}"
            file_path = path / filename
            content = report(format=fmt)
            file_path.write_text(content)
    else:
        # If a single file path is provided, we just save the first format or markdown
        fmt = formats[0] if formats else "markdown"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(format=fmt))
