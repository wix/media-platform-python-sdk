from jose import jwt

from media_platform.auth.token import Token


def sign_jwt(token: Token, secret: str) -> str:
    return jwt.encode(token.to_claims(), secret, algorithm='HS256')


def decode_jwt(shared_secret: str, urn: str, signed_token: str) -> Token:
    claims = jwt.decode(signed_token, shared_secret, subject=urn, options={
        'verify_aud': False
    })

    return Token.from_claims(claims)
