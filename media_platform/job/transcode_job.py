from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.job.transcode.audio_qualities import AudioQuality
from media_platform.job.transcode.stream_specification import StreamSpecification
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.service.destination import Destination


class TranscodeSpecification(Specification):
    def __init__(self, destination, video=None, audio=None, quality_range=None, quality=None):
        # type: (Destination, StreamSpecification, StreamSpecification, VideoQualityRange, AudioQuality or VideoQuality) -> None
        super(Specification, self).__init__()

        self.destination = destination
        self.video = video
        self.audio = audio
        self.quality_range = quality_range
        self.quality = quality

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> TranscodeSpecification

        destination = Destination.deserialize(data['destination'])

        video_data = data.get('video')
        video = StreamSpecification.deserialize(video_data) if video_data else None

        audio_data = data.get('audio')
        audio = StreamSpecification.deserialize(audio_data) if audio_data else None

        quality_range_data = data.get('qualityRange')
        quality_range = VideoQualityRange.deserialize(quality_range_data) if quality_range_data else None

        return TranscodeSpecification(destination, video, audio, quality_range, data.get('quality'))

    def serialize(self):
        # type: () -> dict
        return {
            'destination': self.destination.serialize(),
            'video': self.video.serialize() if self.video else None,
            'audio': self.audio.serialize() if self.audio else None,
            'qualityRange': self.quality_range.serialize() if self.quality_range else None,
            'quality': self.quality
        }

    def validate(self):
        if self.video or self.audio:
            if self.quality_range or self.quality:
                raise ValueError('Multiple transcode specifications')
        elif self.quality_range and self.quality:
            raise ValueError('Multiple transcode specifications')

        if self.quality and not VideoQuality.has_value(self.quality) and not AudioQuality.has_value(self.quality):
            raise ValueError('Quality %s not supported' % self.quality)


class TranscodeJob(Job):
    type = 'urn:job:av.transcode'
    specification_type = TranscodeSpecification
