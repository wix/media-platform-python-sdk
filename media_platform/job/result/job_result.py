from media_platform.lang.serialization import Serializable, Deserializable


class JobResult(Serializable, Deserializable):
    type = None

    def __init__(self, code=None, message=None):
        # type: (int, str) -> None
        self.code = code or 0
        self.message = message or 'OK'

    @classmethod
    def deserialize(cls, data):
        # type: (dict or None) -> JobResult or None
        if not data:
            return None

        return cls(data['code'], data['message'])

    def serialize(self):
        # type: () -> dict
        return {
            'code': self.code,
            'message': self.message
        }
