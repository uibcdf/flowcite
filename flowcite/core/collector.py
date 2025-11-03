from __future__ import annotations

from typing import Any


class Collector:
    # set of target names actually used
    used_targets: set[str] = set()
    # item_id -> list of targets that caused it
    used_items: dict[str, list[str]] = {}

    @classmethod
    def track_target(cls, target: str) -> None:
        cls.used_targets.add(target)

    @classmethod
    def track_item(cls, item_id: str, used_by: str | None = None) -> None:
        cls.used_items.setdefault(item_id, [])
        if used_by is not None and used_by not in cls.used_items[item_id]:
            cls.used_items[item_id].append(used_by)

    @classmethod
    def get_used_items(cls) -> dict[str, list[str]]:
        return cls.used_items.copy()


def track_target(target: str) -> None:
    Collector.track_target(target)


def track_item(item_id: str, used_by: str | None = None) -> None:
    Collector.track_item(item_id, used_by=used_by)


def get_used_items() -> dict[str, list[str]]:
    return Collector.get_used_items()

