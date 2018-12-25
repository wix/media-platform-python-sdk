from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.metadata.audio.audio_extra_metadata import AudioExtraMetadata
from media_platform.service.destination import Destination
from media_platform.service.source import Source


class ReplaceAudioExtraMetadataSpecification(Specification):
    def __init__(self, source, destination, audio_extra_metadata):
        # type: (Source, Destination, AudioExtraMetadata) -> None
        self.source = source
        self.destination = destination
        self.audio_extra_metadata = audio_extra_metadata

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ReplaceAudioExtraMetadataSpecification
        return cls(
            Source.deserialize(data['source']),
            Destination.deserialize(data['destination']),
            AudioExtraMetadata.deserialize(data['audioExtraMetadata'])
        )

    def serialize(self):
        # type: () -> dict
        return {
            'source': self.source.serialize(),
            'destination': self.destination.serialize(),
            'audioExtraMetadata': self.audio_extra_metadata.serialize()
        }


class ReplaceExtraMetadataJob(Job):
    type = 'urn:job:av.replace_extra_metadata'
    specification_type = ReplaceAudioExtraMetadataSpecification
