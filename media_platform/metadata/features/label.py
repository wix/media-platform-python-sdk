from media_platform.lang.serialization import Deserializable


class Label(Deserializable):
    def __init__(self, name, score):
        # type: (str, float) -> None
        super(Label, self).__init__()
        self.name = name
        self.score = score

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Label
        return Label(data['name'], data['score'])
