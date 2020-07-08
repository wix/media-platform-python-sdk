from unittest import TestCase

from media_platform.job.extract_poster_job import ExtractPosterSpecification, PosterFilter, PixelFormat, \
    PosterImageFormat
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL


class TestExtractPosterSpecification(TestCase):

    def test_serialize(self):
        data = {
            'second': 0.12,
            'percentage': None,
            'destination': {
                'path': '/poster.png',
                'acl': 'public',
                'directory': None,
                'lifecycle': None,
                'bucket': None
            },
            'format': 'png',
            'filters': []
        }

        specification = ExtractPosterSpecification(0.12, Destination('/poster.png', acl=ACL.public),
                                                   PosterImageFormat.png)
        self.assertEqual(data, specification.serialize())

    def test_serialize__with_percentage(self):
        data = {
            'second': None,
            'percentage': 10,
            'destination': {
                'path': '/poster.png',
                'acl': 'public',
                'directory': None,
                'lifecycle': None,
                'bucket': None
            },
            'format': 'png',
            'filters': []
        }

        specification = ExtractPosterSpecification(None, Destination('/poster.png', acl=ACL.public),
                                                   PosterImageFormat.png, 10)
        self.assertEqual(data, specification.serialize())

    def test_serialize__with_filters_and_pixel_format(self):
        data = {
            'second': 0.12,
            'percentage': None,
            'destination': {
                'path': '/poster.png',
                'acl': 'public',
                'directory': None,
                'lifecycle': None,
                'bucket': None
            },
            'format': 'png',
            'filters': ['transparentCrop'],
            'pixelFormat': 'rgba'
        }

        specification = ExtractPosterSpecification(
            0.12, Destination('/poster.png', acl=ACL.public), PosterImageFormat.png,
            filters=[PosterFilter.transparent_crop], pixel_format=PixelFormat.rgba)
        self.assertEqual(data, specification.serialize())

    def test_deserialize(self):
        data = {
            'second': 0.12,
            'percentage': None,
            'destination': {
                'path': '/poster.png',
                'acl': 'public',
                'directory': None,
                'lifecycle': None,
                'bucket': None
            },
            'format': 'png',
            'filters': []
        }

        specification = ExtractPosterSpecification.deserialize(data)
        self.assertEqual(data, specification.serialize())

    def test_deserialize__invalid_image_format(self):
        data = {
            'second': 0.12,
            'destination': {
                'path': '/poster.bmp',
                'acl': 'public',
                'directory': None,
                'lifecycle': None,
                'bucket': None
            },
            'format': 'bmp',
            'filters': []
        }

        with self.assertRaises(ValueError):
            ExtractPosterSpecification.deserialize(data).validate()
