from __future__ import annotations

def render(used: dict[str, list[str]], items: dict[str, dict]) -> str:
    lines: list[str] = ["# Workflow Citations and Acknowledgements", ""]
    if not used:
        lines.append("_No items were tracked in this session._")
        return "\n".join(lines)

    for item_id, used_by in used.items():
        item = items.get(item_id, {"title": item_id})
        title = item.get("title", item_id)
        year = item.get("year")
        line = f"- {title}"
        if year:
            line += f" ({year})"
        lines.append(line)
        if used_by:
            lines.append(f"  - Used by: {', '.join(used_by)}")
        note = item.get("note")
        if note:
            lines.append(f"  - Note: {note}")
        lines.append("")
    return "\n".join(lines)

