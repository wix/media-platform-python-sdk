from media_platform.lang.serialization import Deserializable


class ExplicitContent(Deserializable):
    def __init__(self, name, likelihood):
        # type: (str, str) -> None
        super(ExplicitContent, self).__init__()
        self.name = name
        self.likelihood = likelihood

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExplicitContent
        return ExplicitContent(data['name'], data['likelihood'])
