from unittest import TestCase
from hamcrest import *

from media_platform.service.callback import Callback


class TestCallback(TestCase):

    def test_serialize(self):
        callback = Callback('url', {'fish': 'dog'}, {'Me': 'You'})

        assert_that(callback.serialize(), is_({
            'url': 'url',
            'headers': {'Me': 'You'},
            'attachment': {'fish': 'dog'},
            'passthrough': False
        }))

    def test_deserialize(self):
        data = {
            'url': 'url',
            'headers': {'Me': 'You'},
            'attachment': {'fish': 'dog'},
            'passthrough': False
        }

        callback = Callback.deserialize(data)

        assert_that(callback.serialize(), is_(data))
