from media_platform.auth.jwt_coder import sign_jwt, decode_jwt
from media_platform.auth.token import Token


class AppAuthenticator(object):
    def __init__(self, app_id, shared_secret):
        # type: (str, str) -> None

        self._shared_secret = shared_secret
        self._app_urn = 'urn:app:' + app_id

    def default_token(self):
        # type: () -> Token

        return Token(self._app_urn, self._app_urn)

    def default_signed_token(self):
        # type: () -> str
        token = self.default_token()

        return self.sign_token(token)

    def sign_token(self, token):
        # type: (Token) -> str

        return sign_jwt(token, self._shared_secret)

    def decode_token(self, signed_token):
        # type: (str) -> Token

        return decode_jwt(self._shared_secret, self._app_urn, signed_token)
