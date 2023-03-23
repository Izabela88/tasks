from enum import StrEnum


class TileStatus(StrEnum):
    LIVE = "LIVE"
    PENDING = "PENDING"
    ARCHIVED = "ARCHIVED"

    @classmethod
    def choices(cls):
        return ((key.name, key.value) for key in cls)
