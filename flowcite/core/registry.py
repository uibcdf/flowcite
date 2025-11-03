from __future__ import annotations

from typing import TypedDict, Literal, Any


class CitationItem(TypedDict, total=False):
    id: str
    type: Literal["article", "software", "repo", "web", "dataset", "other"]
    title: str
    authors: list[str]
    year: int
    doi: str
    url: str
    note: str
    how_to_cite: str


class Registry:
    # item_id -> item
    items: dict[str, CitationItem] = {}
    # target -> [item_id, ...]
    bindings: dict[str, list[str]] = {}
    # external module -> [item_id, ...]
    injections: dict[str, list[str]] = {}

    @classmethod
    def register_item(cls, **item: Any) -> None:
        item_id = item["id"]
        cls.items[item_id] = item  # overwrite allowed
        # no return

    @classmethod
    def bind(cls, target: str, items: list[str]) -> None:
        cls.bindings.setdefault(target, [])
        for it in items:
            if it not in cls.bindings[target]:
                cls.bindings[target].append(it)

    @classmethod
    def add_injection(cls, target_module: str, items: list[str]) -> None:
        cls.injections.setdefault(target_module, [])
        for it in items:
            if it not in cls.injections[target_module]:
                cls.injections[target_module].append(it)


# convenience functions
def register_item(**item: Any) -> None:
    Registry.register_item(**item)


def bind(target: str, items: list[str]) -> None:
    Registry.bind(target, items)


def add_injection(target_module: str, items: list[str]) -> None:
    Registry.add_injection(target_module, items)
