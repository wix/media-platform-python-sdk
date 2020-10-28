from __future__ import annotations

from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.lang.serialization import Serializable, Deserializable


class RestResult(Serializable, Deserializable):
    def __init__(self, code: int, message: str, payload: dict or list = None):
        self.code = code
        self.message = message
        self.payload = payload

    @classmethod
    def deserialize(cls, data: dict) -> RestResult:
        return RestResult(data['code'], data['message'], data.get('payload'))

    def serialize(self) -> dict:
        return {
            'code': self.code,
            'message': self.message,
            'payload': self.payload
        }

    def raise_for_code(self):
        if self.code != 0:
            # todo: code -> exception mapper
            raise MediaPlatformException()
