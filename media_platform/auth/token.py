from __future__ import annotations

import binascii
import os
import time


class Token:
    def __init__(self, issuer: str, subject: str, verbs: [str] = None, issued_at: int = None, expiration: int = None,
                 additional_claims: dict = None, token_id: str = None):
        self.issuer = issuer
        self.subject = subject

        self.verbs = verbs or list()
        self.issued_at = issued_at or (int(time.time()) - 10)
        self.expiration = expiration or (self.issued_at + 600)
        self.additional_claims = Token._extract_additional_claims(additional_claims) if additional_claims else dict()
        self.id = token_id or binascii.hexlify(os.urandom(6)).decode('utf-8')

    @staticmethod
    def from_claims(data: dict) -> Token:
        additional_claims = Token._extract_additional_claims(data)

        return Token(data['iss'], data['sub'], data.get('aud'), data.get('iat'), data.get('exp'),
                     additional_claims, data.get('jti'))

    def to_claims(self) -> dict:
        data = {
            'iss': self.issuer,
            'sub': self.subject,
            'aud': self.verbs if self.verbs else list(),
            'iat': self.issued_at,
            'exp': self.expiration,
            'jti': self.id
        }

        data.update(self.additional_claims)

        return data

    @staticmethod
    def _extract_additional_claims(claims: dict) -> dict:
        return {k: v for k, v in claims.items() if k not in ['iss', 'sub', 'aud', 'iat', 'exp', 'jti']}
