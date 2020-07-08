class Serializable:

    def serialize(self) -> dict:
        raise NotImplementedError()


class Deserializable:

    @classmethod
    def deserialize(cls, data: dict) -> object:
        raise NotImplementedError()
