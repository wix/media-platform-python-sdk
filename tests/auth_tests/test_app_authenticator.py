import time
import unittest

from hamcrest import assert_that, is_, not_none

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.auth.token import Token


class TestAuthenticator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.shared_secret = '95eee2c63ac2d15270628664c84f6ddd'
        cls.app_id = 'app-id'
        cls.authenticator = AppAuthenticator(cls.app_id, cls.shared_secret)

    def test_default_signed_token(self):
        signed_token = self.authenticator.default_signed_token()

        assert_that(signed_token, not_none())

    def test_from_claims_and_decode(self):
        now = int(time.time() - 10)
        later = now + 10

        app_urn = 'urn:app:%s' % self.app_id
        token = Token(app_urn, app_urn, ['urn:service:file.upload'], now, later, {'fish': 'cat'}, 'id!')

        signed_token = self.authenticator.sign_token(token)

        decoded_token = self.authenticator.decode_token(signed_token)

        assert_that(decoded_token.to_claims(), is_({'sub': app_urn,
                                                    'iss': app_urn,
                                                    'fish': 'cat',
                                                    'jti': 'id!',
                                                    'exp': later,
                                                    'iat': now,
                                                    'aud': ['urn:service:file.upload']
                                                    }))
