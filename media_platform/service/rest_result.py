class RestResult(object):
    def __init__(self, code, message, payload=None):
        # type: (int, str, dict) -> None
        super(RestResult, self).__init__()

        self.code = code
        self.message = message
        self.payload = payload

    @classmethod
    def deserialize(cls, data):
        return RestResult(data['code'], data['message'], data['payload'])
