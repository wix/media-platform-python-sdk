from unittest import TestCase
from hamcrest import *

from media_platform.service.lifecycle import Lifecycle, Action


class TestLifecycle(TestCase):

    def test_serialize(self):
        lifecycle = Lifecycle(age=500, action=Action.delete)

        assert_that(lifecycle.serialize(), is_({
            'age': 500,
            'action': 'delete'
        }))

    def test_deserialize(self):
        data = {
            'age': 500,
            'action': 'delete'
        }

        lifecycle = Lifecycle.deserialize(data)

        assert_that(lifecycle.serialize(), is_(data))
