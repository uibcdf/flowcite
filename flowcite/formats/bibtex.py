from __future__ import annotations

def render(used: dict[str, list[str]], items: dict[str, dict]) -> str:
    # very naive bibtex-like stub
    entries: list[str] = []
    for item_id in used:
        item = items.get(item_id, {"title": item_id})
        key = item_id.replace(":", "_")
        title = item.get("title", "")
        year = item.get("year", "")
        entries.append(f"@misc{{{key},\n  title = {{{title}}},\n  year = {{{year}}}\n}}")
    return "\n\n".join(entries)
