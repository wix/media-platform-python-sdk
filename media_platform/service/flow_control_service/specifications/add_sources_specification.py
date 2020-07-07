from __future__ import annotations

from media_platform.service.source import Source
from media_platform.job.specification import Specification


class AddSourcesSpecification(Specification):
    def __init__(self, sources: [Source]):
        self.sources = sources

    def serialize(self) -> dict:
        return {
            'sources': [s.serialize() for s in self.sources]
        }

    @classmethod
    def deserialize(cls, data: dict) -> AddSourcesSpecification:
        return cls([Source.deserialize(s) for s in data['sources']])
