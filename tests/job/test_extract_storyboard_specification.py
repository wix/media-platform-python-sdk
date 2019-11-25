from unittest import TestCase
from hamcrest import *

from media_platform.job.extract_storyboard_job import ExtractStoryboardSpecification
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL


class TestExtractStoryboardSpecification(TestCase):

    def test_serialize(self):
        data = {
            'columns': 1,
            'rows': 2,
            'tileWidth': 100,
            'tileHeight': 200,
            'format': 'png',
            'segmentDuration': 12.3,
            'destination': {
                'directory': None,
                'path': '/poster.png',
                'lifecycle': None,
                'acl': 'public',
                'bucket': None
            },
        }

        specification = ExtractStoryboardSpecification(Destination('/poster.png', acl=ACL.public), 1, 2, 100, 200,
                                                       'png', 12.3)
        assert_that(specification.serialize(), is_(data))

    def test_deserialize(self):
        data = {
            'columns': 1,
            'rows': 2,
            'tileWidth': 100,
            'tileHeight': 200,
            'format': 'png',
            'segmentDuration': 12.3,
            'destination': {
                'directory': None,
                'path': '/poster.png',
                'lifecycle': None,
                'acl': 'public',
                'bucket': None
            },
        }

        specification = ExtractStoryboardSpecification.deserialize(data)
        assert_that(specification.serialize(), is_(data))

    def test_invalid_image_format(self):
        data = {
            'columns': 1,
            'rows': 2,
            'tileWidth': 100,
            'tileHeight': 200,
            'format': 'tiff',
            'segmentDuration': 12.3,
            'destination': {
                'directory': None,
                'path': '/poster.png',
                'lifecycle': None,
                'acl': 'public',
                'bucket': None
            },
        }

        with self.assertRaises(ValueError):
            ExtractStoryboardSpecification.deserialize(data).validate()

    def test_jpeg_overflow_width(self):
        data = {
            'columns': 10,
            'rows': 2,
            'tileWidth': 10000,
            'tileHeight': 200,
            'format': 'jpg',
            'segmentDuration': 12.3,
            'destination': {
                'directory': None,
                'path': '/poster.png',
                'lifecycle': None,
                'acl': 'public',
                'bucket': None
            },
        }

        with self.assertRaises(ValueError):
            ExtractStoryboardSpecification.deserialize(data).validate()

    def test_jpeg_overflow_height(self):
        data = {
            'columns': 1,
            'rows': 20,
            'tileWidth': 100,
            'tileHeight': 20000,
            'format': 'jpg',
            'segmentDuration': 12.3,
            'destination': {
                'directory': None,
                'path': '/poster.png',
                'lifecycle': None,
                'acl': 'public',
                'bucket': None
            },
        }

        with self.assertRaises(ValueError):
            ExtractStoryboardSpecification.deserialize(data).validate()
