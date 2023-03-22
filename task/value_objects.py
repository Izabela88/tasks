from enum import StrEnum


class TileStatus(StrEnum):
    LIVE = "live"
    PENDING = "pending"
    ARCHIVED = "archived"

    @classmethod
    def choices(cls):
        return ((key.name, key.value) for key in cls)
