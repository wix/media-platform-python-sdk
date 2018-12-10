from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.job.transcode.audio_qualities import AudioQualities
from media_platform.job.transcode.stream_specification import StreamSpecification
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.lang import datetime_serialization
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source


class TranscodeSpecification(Specification):
    def __init__(self, destination, video=None, audio=None, quality_range=None, quality=None):
        # type: (Destination, StreamSpecification, StreamSpecification, VideoQualityRange, AudioQualities or VideoQuality) -> None
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

        if self.quality and not VideoQuality.has_value(self.quality) and not AudioQualities.has_value(self.quality):
            raise ValueError('Quality %s not supported' % self.quality)


class TranscodeJob(Job):
    type = 'urn:job:av.transcode'

    def __init__(self, job_id, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        super(TranscodeJob, self).__init__(job_id, self.type, issuer, status, specification, sources,
                                           callback, flow_id, result, date_created, date_updated)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> TranscodeJob

        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        specification = TranscodeSpecification.deserialize(data['specification'])
        if data.get('result'):
            result = RestResult.deserialize(data['result'])
        else:
            result = None

        return cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                   data.get('flowId'), result, date_created, date_updated)
