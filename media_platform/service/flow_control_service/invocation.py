from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.source import Source


class Invocation(Serializable, Deserializable):
    def __init__(self, entry_points, sources=None):
        # type: ([str], [Source]) -> None
        super(Invocation, self).__init__()

        self.entry_points = entry_points
        self.sources = sources or []

    def serialize(self):
        # type: () -> dict
        return {
            'entryPoints': self.entry_points,
            'sources': [source.serialize() for source in self.sources]
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Invocation
        sources = [Source.deserialize(s) for s in data['sources']]

        return Invocation(data['entryPoints'], sources)
