class Serializable(object):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Serializable
        raise NotImplementedError()

    def serialize(self):
        # type: () -> dict
        raise NotImplementedError()
