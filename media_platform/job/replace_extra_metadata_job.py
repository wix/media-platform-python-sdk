from __future__ import annotations

from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.service.audio_service.audio_extra_metadata import AudioExtraMetadata
from media_platform.service.destination import Destination


class ReplaceAudioExtraMetadataSpecification(Specification):
    def __init__(self, destination: Destination, audio_extra_metadata: AudioExtraMetadata):
        self.destination = destination
        self.audio_extra_metadata = audio_extra_metadata

    @classmethod
    def deserialize(cls, data: dict) -> ReplaceAudioExtraMetadataSpecification:
        return cls(
            Destination.deserialize(data['destination']),
            AudioExtraMetadata.deserialize(data['audioExtraMetadata'])
        )

    def serialize(self) -> dict:
        return {
            'destination': self.destination.serialize(),
            'audioExtraMetadata': self.audio_extra_metadata.serialize()
        }


class ReplaceExtraMetadataJob(Job):
    type = 'urn:job:av.replace_extra_metadata'
    specification_type = ReplaceAudioExtraMetadataSpecification
