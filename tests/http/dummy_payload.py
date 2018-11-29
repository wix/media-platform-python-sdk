from media_platform.lang.serializable import Serializable


class DummyPayload(Serializable):
    def __init__(self, dumdum=None):
        # type: (str) -> None
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
