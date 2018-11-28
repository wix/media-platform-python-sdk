import unittest

from hamcrest import assert_that, instance_of

import media_platform
from media_platform import MediaPlatformClient


class TestStringMethods(unittest.TestCase):

    def test_init(self):

        client = media_platform.Client('domain', 'app', 'secret')

        assert_that(client, instance_of(MediaPlatformClient))
