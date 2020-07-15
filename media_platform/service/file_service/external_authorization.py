from __future__ import annotations

from media_platform.lang.serialization import Serializable


class ExternalAuthorization(Serializable):
    def __init__(self, headers: dict):
        super(ExternalAuthorization, self).__init__()
        self.headers = headers

    def serialize(self) -> dict:
        return {
            'headers': self.headers
        }

    @classmethod
    def deserialize(cls, data: dict) -> ExternalAuthorization:
        return cls(data['headers'])
