from datetime import datetime
from unittest import TestCase

from hamcrest import assert_that, is_

from media_platform.lang import datetime_serialization


class TestDatetimeSerializer(TestCase):

    def test_deserialize_with_millis(self):
        time_string = '2002-12-25T00:00:00.000000Z'

        time = datetime_serialization.deserialize(time_string)

        assert_that(time, is_(datetime(2002, 12, 25)))

    def test_deserialize(self):
        time_string = '2002-12-25T00:00:00Z'

        time = datetime_serialization.deserialize(time_string)

        assert_that(time, is_(datetime(2002, 12, 25)))

    def test_serialize(self):
        date = datetime(2002, 12, 25)

        time_string = datetime_serialization.serialize(date)

        assert_that(time_string, is_('2002-12-25T00:00:00Z'))
