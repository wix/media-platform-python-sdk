from unittest import TestCase
from hamcrest import assert_that, is_

from media_platform.metadata.image.image_features import ImageFeatures


class TestImageFeatures(TestCase):

    def test_serialize_deserialize_with_explicit_content(self):
        data = {
            'labels': [
                {'name': 'one', 'score': 0.2323},
                {'name': 'two', 'score': 0.9}
            ],
            'faces': [
                {'x': 383, 'y': 393, 'width': 155, 'height': 180},
                {'x': 460, 'y': 385, 'width': 145, 'height': 173}
            ],
            'colors': [
                {'r': 138, 'g': 218, 'b': 244, 'pixelFraction': 0.38548386, 'score': 0.688166},
            ],
            'explicitContent': [
                {
                    'name': 'adult',
                    'likelihood': 'VERY_UNLIKELY'
                }
            ]
        }

        image_features = ImageFeatures.deserialize(data)

        assert_that(len(image_features.labels), is_(2))
        assert_that(len(image_features.faces), is_(2))
        assert_that(len(image_features.colors), is_(1))
        assert_that(len(image_features.explicit_content), is_(1))
