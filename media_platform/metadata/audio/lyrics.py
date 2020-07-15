from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class Lyrics(Serializable, Deserializable):
    def __init__(self, text: str, language: str = None, description: str = None):
        self.description = description
        self.language = language
        self.text = text

    def serialize(self) -> dict:
        return {
            'text': self.text,
            'description': self.description,
            'language': self.language,
        }

    @classmethod
    def deserialize(cls, data: dict) -> Lyrics:
        return cls(data['text'], data.get('language') or data.get('lang'), data.get('description'))
