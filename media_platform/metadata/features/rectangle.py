from __future__ import annotations

from media_platform.lang.serialization import Deserializable


class Rectangle(Deserializable):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def deserialize(cls, data: dict) -> Rectangle:
        return Rectangle(data['x'], data['y'], data['width'], data['height'])
