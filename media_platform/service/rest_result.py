from exception.media_platform_exception import MediaPlatformException
from media_platform.lang.serializable_deserializable import Serializable, Deserializable


class RestResult(Serializable, Deserializable):
    def __init__(self, code, message, payload=None):
        # type: (int, str, dict) -> None

        self.code = code
        self.message = message
        self.payload = payload

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> RestResult
        return RestResult(data['code'], data['message'], data['payload'])

    def serialize(self):
        return {
            'code': self.code,
            'message': self.message,
            'payload': self.payload
        }

    def raise_for_code(self):
        if self.code != 0:
            # todo: code -> exception mapper (Alon, have fun :))
            raise MediaPlatformException()
