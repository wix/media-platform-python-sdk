import unittest

from hamcrest import assert_that, instance_of

import media_platform

from media_platform.media_platform_client import MediaPlatformClient


class TestClient(unittest.TestCase):

    def test_init(self):
        client = media_platform.Client('domain', 'app', 'secret')

        assert_that(client, instance_of(MediaPlatformClient))
