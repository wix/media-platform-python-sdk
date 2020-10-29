from __future__ import annotations

from media_platform.lang.serialization import Deserializable


class ExplicitContent(Deserializable):
    def __init__(self, name: str, likelihood: str):
        self.name = name
        self.likelihood = likelihood

    @classmethod
    def deserialize(cls, data: dict) -> ExplicitContent:
        return ExplicitContent(data['name'], data['likelihood'])
