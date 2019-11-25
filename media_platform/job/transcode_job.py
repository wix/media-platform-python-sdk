from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.job.transcode.audio_qualities import AudioQuality
from media_platform.job.transcode.clipping import Clipping
from media_platform.job.transcode.stream_specification import StreamSpecification
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.service.destination import Destination


class TranscodeSpecification(Specification):
    def __init__(self, destination, video=None, audio=None, quality_range=None, quality=None, clipping=None):
        # type: (Destination, StreamSpecification, StreamSpecification, VideoQualityRange, AudioQuality or VideoQuality, Clipping or None) -> None
        super(Specification, self).__init__()

        self.destination = destination
        self.video = video
        self.audio = audio
        self.quality_range = quality_range
        self.quality = quality
        self.clipping = clipping

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

        quality = data.get('quality')

        clipping_data = data.get('clipping')
        clipping = Clipping.deserialize(clipping_data) if clipping_data else None

        return TranscodeSpecification(destination, video, audio, quality_range, quality, clipping)

    def serialize(self):
        # type: () -> dict
        return {
            'destination': self.destination.serialize(),
            'video': self.video.serialize() if self.video else None,
            'audio': self.audio.serialize() if self.audio else None,
            'qualityRange': self.quality_range.serialize() if self.quality_range else None,
            'quality': self.quality,
            'clipping': self.clipping.serialize() if self.clipping else None
        }

    def validate(self):
        stream_specified = (self.video or self.audio)
        quality_specified = (self.quality_range or self.quality)

        if self.quality_range:
            self.quality_range.validate()

        if self.video:
            self.video.validate()

        if self.audio:
            self.video.validate()

        if stream_specified and quality_specified:
            raise ValueError('Either stream specification or quality may be specified, not both')

        if self.quality_range and self.quality:
            raise ValueError('Either quality range or quality may be specified, not both')

        if self.quality and not VideoQuality.has_value(self.quality) and not AudioQuality.has_value(self.quality):
            raise ValueError('Quality %s is not supported' % self.quality)

        if not stream_specified and not quality_specified and not self.clipping:
            raise ValueError('Either video, audio, quality range, quality or clipping must be specified')


class TranscodeJob(Job):
    type = 'urn:job:av.transcode'
    specification_type = TranscodeSpecification

