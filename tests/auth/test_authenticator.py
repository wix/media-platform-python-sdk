import time
import unittest

from hamcrest import assert_that, is_, not_none

from media_platform.auth.authenticator import Authenticator
from media_platform.auth.token import Token
from media_platform.configuration.configuration import Configuration


class TestAuthenticator(unittest.TestCase):
    configuration = Configuration('domain', 'app-id', '95eee2c63ac2d15270628664c84f6ddd')

    authenticator = Authenticator(configuration)

    def test_default_signed_token(self):
        signed_token = self.authenticator.default_signed_token()

        assert_that(signed_token, not_none())

    def test_from_claims_and_decode(self):
        now = int(time.time() - 10)
        later = now + 10

        token = Token('urn:app:app-id', 'urn:app:app-id', ['urn:service:file.upload'], now, later, {'fish': 'cat'},
                      'id!')

        signed_token = self.authenticator.sign_token(token)

        decoded_token = self.authenticator.decode_token(signed_token)

        assert_that(decoded_token.to_claims(), is_({'sub': 'urn:app:app-id',
                                                    'iss': 'urn:app:app-id',
                                                    'fish': 'cat',
                                                    'jti': 'id!',
                                                    'exp': later,
                                                    'iat': now,
                                                    'aud': ['urn:service:file.upload']
                                                    }))
