from __future__ import annotations

from media_platform.job.job import Job
from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.service.destination import Destination

# todo: proper class
SUPPORTED_IMAGE_FORMATS = ['jpg', 'png']


class ExtractStoryboardSpecification(Specification):
    def __init__(self, destination: Destination, columns: int, rows: int, tile_width: int = None,
                 tile_height: int = None, image_format: str = 'jpg', segment_duration: float = None):
        self.destination = destination
        self.columns = columns
        self.rows = rows
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.image_format = image_format
        self.segment_duration = segment_duration

    @classmethod
    def deserialize(cls, data: dict) -> ExtractStoryboardSpecification:
        destination = Destination.deserialize(data['destination'])

        return ExtractStoryboardSpecification(destination, data['columns'], data['rows'], data.get('tileWidth'),
                                              data.get('tileHeight'), data.get('format'), data.get('segmentDuration'))

    def serialize(self) -> dict:
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
    def _validate_max_jpeg_size(tiles: int, pixels: int):
        if tiles * pixels > 65534:
            raise ValueError('jpeg supports up to 65k pixels')


class ExtractStoryboardJob(Job):
    type = JobType.extract_storyboard
    specification_type = ExtractStoryboardSpecification
