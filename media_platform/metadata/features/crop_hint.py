from __future__ import annotations

from media_platform.metadata.features.rectangle import Rectangle


class CropHint(Rectangle):
    def __init__(self, x: int, y: int, width: int, height: int, confidence: float, importance_fraction: float):
        super().__init__(x, y, width, height)
        self.confidence = confidence
        self.importance_fraction = importance_fraction

    @classmethod
    def deserialize(cls, data: dict) -> CropHint:
        return CropHint(data['x'], data['y'], data['width'], data['height'], data['confidence'],
                        data['importanceFraction'])
