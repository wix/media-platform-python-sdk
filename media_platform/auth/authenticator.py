import logging

from jose import jwt

from media_platform.auth.token import Token
from media_platform.configuration.configuration import Configuration


class Authenticator(object):
    def __init__(self, configuration):
        # type: (Configuration) -> None
        super(Authenticator, self).__init__()

        self.configuration = configuration

        self.urn = "urn:app:" + self.configuration.app_id

    def default_signed_token(self):
        # type: () -> str

        token = Token(self.urn, self.urn)

        return self.sign_token(token)

    def sign_token(self, token):
        # type: (Token) -> str

        return jwt.encode(token.to_claims(), self.configuration.shared_secret, algorithm='HS256')

    def decode_token(self, signed_token):
        # type: (str) -> Token or None
        token = None

        # noinspection PyBroadException
        try:
            claims = jwt.decode(signed_token, self.configuration.shared_secret, subject=self.urn, options={
                'verify_aud': False
            })

            token = Token.from_claims(claims)
        except Exception:
            logging.exception('failed to decode signed token %s: ' % signed_token)

        return token
