from __future__ import annotations

from media_platform.lang.serialization import Deserializable


class Label(Deserializable):
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    @classmethod
    def deserialize(cls, data: dict) -> Label:
        return Label(data['name'], data['score'])
