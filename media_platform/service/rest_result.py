from media_platform.lang.serializable import Serializable


class RestResult(Serializable):
    def __init__(self, code, message, payload=None):
        # type: (int, str, dict) -> None
        super(RestResult, self).__init__()

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
