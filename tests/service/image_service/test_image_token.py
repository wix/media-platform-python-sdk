import unittest

from hamcrest import assert_that, is_

from media_platform.service.image_service.image_token import Policy, Watermark, Gravity, ImageToken


class TestImageToken(unittest.TestCase):

    def test_policy_to_claim(self):
        policy = Policy('/moshe.jpg', 100, 200)

        assert_that(policy.to_claim(), is_({
            'obj': [
                [
                    {
                        'path': '/moshe.jpg',
                        'width': '<=100',
                        'height': '<=200'
                    }
                ]
            ]
        }))

    def test_watermark_to_claim(self):
        watermark = Watermark('/chaim.jpg', 40, 0.1, Gravity.east)

        assert_that(watermark.to_claim(), is_({
            'wmk': {
                'path': '/chaim.jpg',
                'opacity': 40,
                'proportions': 0.1,
                'gravity': 'east'
            }
        }))

    def test_image_token_to_claims(self):
        token = ImageToken('urn:app:moshe', 'urn:app:moshe', None, None, 100, 200, {'fish': 'cat'}, 'id!')

        assert_that(token.to_claims(), is_({
            'sub': 'urn:app:moshe',
            'iss': 'urn:app:moshe',
            'fish': 'cat',
            'jti': 'id!',
            'exp': 200,
            'iat': 100,
            'aud': ['urn:service:image.operations']
        }))

    def test_image_token_with_watermark_to_claims(self):
        watermark = Watermark('/chaim.jpg', 40, 0.1, Gravity.east)

        token = ImageToken('urn:app:moshe', 'urn:app:moshe', None, watermark, 100, 200, {'fish': 'cat'}, 'id!')

        assert_that(token.to_claims(), is_({
            'wmk': {
                'opacity': 40,
                'path': '/chaim.jpg',
                'proportions': 0.1,
                'gravity': 'east'
            },
            'sub': 'urn:app:moshe',
            'iss': 'urn:app:moshe',
            'fish': 'cat',
            'jti': 'id!',
            'exp': 200,
            'iat': 100,
            'aud': ['urn:service:image.operations']
        }))

    def test_image_token_with_policy_to_claims(self):
        policy = Policy('/moshe.jpg', 100, 200)

        token = ImageToken('urn:app:moshe', 'urn:app:moshe', policy, None, 100, 200, {'fish': 'cat'}, 'id!')

        assert_that(token.to_claims(), is_({
            'obj': [
                [
                    {
                        'path': '/moshe.jpg',
                        'width': '<=100',
                        'height': '<=200'
                    }
                ]
            ],
            'sub': 'urn:app:moshe',
            'iss': 'urn:app:moshe',
            'fish': 'cat',
            'jti': 'id!',
            'exp': 200,
            'iat': 100,
            'aud': ['urn:service:image.operations']
        }))

    def test_image_token_with_policy_to_claims__with_min_blur(self):
        policy = Policy('/moshe.jpg', min_blur=0.5)

        token = ImageToken('urn:app:moshe', 'urn:app:moshe', policy, None, 100, 200, {'fish': 'cat'}, 'id!')

        assert_that(token.to_claims(), is_({
            'obj': [
                [
                    {
                        'path': '/moshe.jpg',
                        'blur': '>=0.5'
                    }
                ]
            ],
            'sub': 'urn:app:moshe',
            'iss': 'urn:app:moshe',
            'fish': 'cat',
            'jti': 'id!',
            'exp': 200,
            'iat': 100,
            'aud': ['urn:service:image.operations']
        }))
