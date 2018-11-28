import binascii
import os
import time


class Token(object):
    def __init__(self, issuer, subject, verbs=None, issued_at=None, expiration=None,
                 additional_claims=None, token_id=None):
        # type: (str, str, [str], long, long, dict, str) -> None
        super(Token, self).__init__()

        self.issuer = issuer
        self.subject = subject

        self.verbs = verbs or list()
        self.issued_at = issued_at or (int(time.time()) - 10)
        self.expiration = expiration or (issued_at + 600)
        self.additional_claims = additional_claims or dict()
        self.id = token_id or binascii.hexlify(os.urandom(6))

    @staticmethod
    def from_claims(data):
        # type: (dict) -> Token
        additional_claims = {}
        additional_claims.update(data)

        del additional_claims['iss']
        del additional_claims['sub']
        del additional_claims['aud']
        del additional_claims['iat']
        del additional_claims['exp']
        del additional_claims['jti']

        return Token(data['iss'], data['sub'], data.get('aud'), data.get('iat'), data.get('exp'),
                     additional_claims, data.get('jti'))

    def to_claims(self):
        # type: () -> dict
        data = {
            'iss': self.issuer,
            'sub': self.subject,
            'aud': self.verbs if self.verbs else None,
            'iat': self.issued_at,
            'exp': self.expiration,
            'jti': self.id
        }

        data.update(self.additional_claims)

        return data
