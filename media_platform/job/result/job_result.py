from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class JobResult(Serializable, Deserializable):
    type = None

    def __init__(self, code: int = None, message: str = None):
        self.code = code or 0
        self.message = message or 'OK'

    @classmethod
    def deserialize(cls, data: dict or None) -> JobResult or None:
        if not data:
            return None

        return cls(data['code'], data['message'])

    def serialize(self) -> dict:
        return {
            'code': self.code,
            'message': self.message
        }
