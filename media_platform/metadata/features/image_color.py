from __future__ import annotations

from media_platform.lang.serialization import Deserializable


class Color(Deserializable):
    def __init__(self, r: int, g: int, b: int, pixel_fraction: float, score: float):
        self.r = r
        self.g = g
        self.b = b
        self.pixel_fraction = pixel_fraction
        self.score = score

    @classmethod
    def deserialize(cls, data: dict) -> Color:
        return Color(data['r'], data['g'], data['b'], data['pixelFraction'], data['score'])
