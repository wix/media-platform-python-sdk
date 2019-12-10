from media_platform.lang.serialization import Serializable


class ExternalAuthorization(Serializable):
    def __init__(self, headers):
        # type: (dict) -> None
        super(ExternalAuthorization, self).__init__()

        self.headers = headers

    def serialize(self):
        return {
            'headers': self.headers
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExternalAuthorization
        return cls(data['headers'])