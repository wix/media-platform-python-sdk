from media_platform.auth.jwt_coder import sign_jwt, decode_jwt
from media_platform.auth.token import Token


class AppAuthenticator:
    def __init__(self, app_id: str, shared_secret: str):
        self._shared_secret = shared_secret
        self._app_urn = 'urn:app:' + app_id

    def default_token(self) -> Token:
        return Token(self._app_urn, self._app_urn)

    def default_signed_token(self) -> str:
        token = self.default_token()

        return self.sign_token(token)

    def sign_token(self, token: Token) -> str:
        return sign_jwt(token, self._shared_secret)

    def decode_token(self, signed_token: str) -> Token:
        return decode_jwt(self._shared_secret, self._app_urn, signed_token)
