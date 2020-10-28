from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class FontBasic(Serializable, Deserializable):
    def __init__(self, font_type: str = None, name: str = None, family: str = None):
        self.font_type = font_type
        self.name = name
        self.family = family

    @classmethod
    def deserialize(cls, data: dict) -> FontBasic:
        return FontBasic(data['fontType'], data.get('name'), data.get('family'))

    def serialize(self) -> dict:
        return {
            'fontType': self.font_type,
            'name': self.name,
            'family': self.family
        }
