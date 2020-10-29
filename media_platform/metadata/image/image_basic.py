from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class ImageBasic(Serializable, Deserializable):
    def __init__(self, width: int = None, height: int = None, image_format: str = None, color_space: str = None):
        self.width = int(width) if width else None
        self.height = int(height) if height else None
        self.format = image_format
        self.color_space = color_space

    @classmethod
    def deserialize(cls, data: dict) -> ImageBasic:
        return ImageBasic(data['width'], data['height'], data['format'], data.get('colorspace'))

    def serialize(self) -> dict:
        return {
            'width': self.width,
            'height': self.height,
            'format': self.format,
            'colorspace': self.color_space
        }
