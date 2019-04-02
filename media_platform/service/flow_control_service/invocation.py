from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.callback import Callback
from media_platform.service.source import Source


class ErrorStrategy(object):
    stop_on_error = 'stopOnError'
    continue_on_error = 'continueOnError'


class Invocation(Serializable, Deserializable):
    def __init__(self, entry_points, sources=None, callback=None, error_strategy=None):
        # type: ([str], [Source], Callback or None, ErrorStrategy) -> None
        super(Invocation, self).__init__()

        self.entry_points = entry_points
        self.sources = sources or []
        self.callback = callback
        self.error_strategy = error_strategy or ErrorStrategy.stop_on_error

    def serialize(self):
        # type: () -> dict
        return {
            'entryPoints': self.entry_points,
            'sources': [source.serialize() for source in self.sources],
            'callback': self.callback.serialize() if self.callback else None,
            'errorStrategy': self.error_strategy
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Invocation
        sources = [Source.deserialize(s) for s in data['sources']]
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None

        return cls(data['entryPoints'], sources, callback, data.get('errorStrategy'))
