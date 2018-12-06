from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.job.job import Job
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source

SUPPORTED_IMAGE_FORMATS = ['jpg', 'png']


class ExtractStoryboardSpecification(Specification):
    def __init__(self, destination, columns, rows, tile_width=None, tile_height=None, image_format='jpg',
                 segment_duration=None):
        # type: (Destination, int, int, int, int, str, float) -> None
        super(ExtractStoryboardSpecification, self).__init__()

        self.destination = destination
        self.columns = columns
        self.rows = rows
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.image_format = image_format
        self.segment_duration = segment_duration

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractStoryboardSpecification
        destination = Destination.deserialize(data['destination'])

        return ExtractStoryboardSpecification(destination, data['columns'], data['rows'], data.get('tileWidth'),
                                              data.get('tileHeight'), data.get('format'), data.get('segmentDuration'))

    def serialize(self):
        # type: () -> dict
        return {
            'destination': self.destination.serialize(),
            'columns': self.columns,
            'rows': self.rows,
            'tileWidth': self.tile_width,
            'tileHeight': self.tile_height,
            'format': self.image_format,
            'segmentDuration': self.segment_duration
        }

    def validate(self):
        if self.image_format not in SUPPORTED_IMAGE_FORMATS:
            raise ValueError('image format must be one of: %s' % ', '.join(SUPPORTED_IMAGE_FORMATS))

        if self.image_format == 'jpg' and self.tile_width:
            self._validate_max_jpeg_size(self.columns, self.tile_width)

        if self.image_format == 'jpg' and self.tile_height:
            self._validate_max_jpeg_size(self.rows, self.tile_height)

    @staticmethod
    def _validate_max_jpeg_size(tiles, pixels):
        # type: (int, int) -> None
        if tiles * pixels > 65534:
            raise ValueError('jpeg supports up to 65k pixels')


class ExtractStoryboardJob(Job):
    type = 'urn:job:av.storyboard'

    def __init__(self, job_id, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        super(ExtractStoryboardJob, self).__init__(job_id, self.type, issuer, status, specification, sources,
                                                   callback, flow_id, result, date_created, date_updated)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractStoryboardJob

        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        specification = ExtractStoryboardSpecification.deserialize(data['specification'])
        if data.get('result'):
            # todo: result payload is FileDescriptor(s)
            result = RestResult.deserialize(data['result'])
        else:
            result = None

        return cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                   data.get('flowId'), result, date_created, date_updated)
