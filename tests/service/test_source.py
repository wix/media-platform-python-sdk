from unittest import TestCase
from hamcrest import *

from media_platform.service.source import Source


class TestSource(TestCase):

    def test_serialize(self):
        source = Source('/fish.jpg')

        assert_that(source.serialize(), is_({
            'fileId': None,
            'path': '/fish.jpg',
        }))

    def test_deserialize(self):
        data = {
            'fileId': None,
            'path': '/fish.jpg',
        }

        source = Source.deserialize(data)

        assert_that(source.serialize(), is_(data))
