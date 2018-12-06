from unittest import TestCase
from hamcrest import *

from media_platform.job.extract_poster_job import ExtractPosterSpecification
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL


class TestExtractPosterSpecification(TestCase):

    def test_serialize(self):
        data = {
            'second': 0.12,
            'destination': {
                'path': '/poster.png',
                'acl': 'public',
                'directory': None,
                'lifecycle': None
            },
            'format': 'png'
        }

        specification = ExtractPosterSpecification(0.12, Destination('/poster.png', acl=ACL.public), 'png')
        assert_that(specification.serialize(), is_(data))

    def test_deserialize(self):
        data = {
            'second': 0.12,
            'destination': {
                'path': '/poster.png',
                'acl': 'public',
                'directory': None,
                'lifecycle': None
            },
            'format': 'png'
        }

        specification = ExtractPosterSpecification.deserialize(data)
        assert_that(specification.serialize(), is_(data))

    def test_invalid_image_format(self):
        data = {
            'second': 0.12,
            'destination': {
                'path': '/poster.bmp',
                'acl': 'public',
                'directory': None,
                'lifecycle': None
            },
            'format': 'bmp'
        }

        with self.assertRaises(ValueError):
            ExtractPosterSpecification.deserialize(data).validate()
