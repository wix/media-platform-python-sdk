import unittest

from hamcrest import assert_that, is_

from media_platform.auth.token import Token


class TestToken(unittest.TestCase):

    def test_to_claims(self):
        token = Token('urn:app:moshe', 'urn:app:moshe', ['urn:service:file.upload'], 100, 200, {'fish': 'cat'}, 'id!')

        assert_that(token.to_claims(), is_({'sub': 'urn:app:moshe',
                                            'iss': 'urn:app:moshe',
                                            'fish': 'cat',
                                            'jti': 'id!',
                                            'exp': 200,
                                            'iat': 100,
                                            'aud': ['urn:service:file.upload']
                                            }))

    def test_from_claims(self):
        token = Token.from_claims({'sub': 'urn:app:moshe',
                                   'iss': 'urn:app:moshe',
                                   'fish': 'cat',
                                   'jti': 'id!',
                                   'exp': 200,
                                   'iat': 100,
                                   'aud': ['urn:service:file.upload']
                                   })

        assert_that(token.to_claims(), is_({'sub': 'urn:app:moshe',
                                            'iss': 'urn:app:moshe',
                                            'fish': 'cat',
                                            'jti': 'id!',
                                            'exp': 200,
                                            'iat': 100,
                                            'aud': ['urn:service:file.upload']
                                            }))
