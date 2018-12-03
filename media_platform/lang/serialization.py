class Serializable(object):

    def serialize(self):
        # type: () -> dict
        raise NotImplementedError()


class Deserializable(object):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> object
        raise NotImplementedError()
