from media_platform.service.source import Source
from media_platform.job.specification import Specification


class AddSourcesSpecification(Specification):
    def __init__(self, sources):
        # type: ([Source]) -> None
        self.sources = sources

    def serialize(self):
        return {
            'sources': [s.serialize() for s in self.sources]
        }

    @classmethod
    def deserialize(cls, data):
        return cls([Source.deserialize(s) for s in data['sources']])
