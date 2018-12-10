from media_platform.job.specification import Specification
from media_platform.job.transcode.audio_specification import AudioSpecification
from media_platform.job.transcode.video_specification import VideoSpecification


class StreamType(object):
    audio = 'audio'
    video = 'video'


class StreamSpecification(Specification):
    def __init__(self, stream_type, specification=None, skip=False, copy=False):
        # type: (StreamType, AudioSpecification or VideoSpecification, bool, bool) -> None
        self.stream_type = stream_type
        self.specification = specification
        self.skip = skip
        self.copy = copy

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> StreamSpecification
        stream_type = data['type']

        skip = data.get('skip', False)
        copy = data.get('copy', False)

        specification_data = data.get('specification')
        if skip or copy or not specification_data:
            specification = None
        elif stream_type == StreamType.audio:
            specification = AudioSpecification.deserialize(specification_data)
        elif stream_type == StreamType.video:
            specification = VideoSpecification.deserialize(specification_data)
        else:
            raise ValueError('Specification stream type %s not supported' % stream_type)

        return StreamSpecification(stream_type, specification, skip, copy)

    def serialize(self):
        # type: () -> dict
        return {
            'type': self.stream_type,
            'skip': self.skip,
            'copy': self.copy,
            'specification': self.specification.serialize() if self.specification else None
        }

    def validate(self):
        if self.specification:
            self.specification.validate()
