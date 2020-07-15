from media_platform.lang.serialization import Serializable, Deserializable


class DummyPayload(Serializable, Deserializable):
    def __init__(self, dumdum: str = None):
        super(DummyPayload, self).__init__()

        self.dumdum = dumdum or 'knucklehead'

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> DummyPayload
        return DummyPayload(data.get('dumdum'))

    def serialize(self):
        return {
            'dumdum': self.dumdum
        }
