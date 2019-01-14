from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.callback import Callback
from media_platform.service.source import Source


class Invocation(Serializable, Deserializable):
    def __init__(self, entry_points, sources=None, callback=None):
        # type: ([str], [Source], Callback or None) -> None
        super(Invocation, self).__init__()

        self.entry_points = entry_points
        self.sources = sources or []
        self.callback = callback

    def serialize(self):
        # type: () -> dict
        return {
            'entryPoints': self.entry_points,
            'sources': [source.serialize() for source in self.sources],
            'callback': self.callback.serialize() if self.callback else None
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Invocation
        sources = [Source.deserialize(s) for s in data['sources']]
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None

        return Invocation(data['entryPoints'], sources, callback)
