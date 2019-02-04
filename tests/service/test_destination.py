from unittest import TestCase
from hamcrest import *

from media_platform.service.destination import Destination


class TestDestination(TestCase):

    def test_serialize(self):
        destination = Destination('/fish.jpg')

        assert_that(destination.serialize(), is_({
            'directory': None,
            'path': '/fish.jpg',
            'lifecycle': None,
            'acl': 'public',
            'bucket': None
        }))

    def test_deserialize(self):
        data = {
            'directory': None,
            'path': '/fish.jpg',
            'lifecycle': None,
            'acl': 'public',
            'bucket': None
        }

        destination = Destination.deserialize(data)

        assert_that(destination.serialize(), is_(data))
