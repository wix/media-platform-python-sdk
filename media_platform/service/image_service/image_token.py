from __future__ import annotations

from media_platform.auth.token import Token

_VERB = 'urn:service:image.operations'


class Gravity:
    center = 'center'
    north = "north"
    north_west = "north-west"
    west = "west"
    south_west = "south-west"
    south = "south"
    south_east = "south-east"
    east = "east"
    north_east = "north-east"


class Watermark:
    def __init__(self, path: str, opacity: int = 50, proportions: float = 0.25, gravity: Gravity = Gravity.center):
        self.path = path
        self.opacity = opacity
        self.proportions = proportions
        self.gravity = gravity

    def to_claim(self) -> dict:
        watermark = {}
        if self.path:
            watermark['path'] = self.path
        if self.opacity:
            watermark['opacity'] = self.opacity
        if self.proportions:
            watermark['proportions'] = self.proportions
        if self.gravity:
            watermark['gravity'] = self.gravity

        return {
            'wmk': watermark
        }


class Policy:
    def __init__(self, path: str, max_width: int = None, max_height: int = None, min_blur: float = None):
        self.path = path
        self.max_width = max_width
        self.max_height = max_height
        self.min_blur = min_blur

    def to_claim(self) -> dict:
        policy = {}
        if self.path:
            policy['path'] = self.path
        if self.max_height:
            policy['height'] = '<=%s' % self.max_height
        if self.max_width:
            policy['width'] = '<=%s' % self.max_width
        if self.min_blur:
            policy['blur'] = '>=%s' % self.min_blur

        return {
            'obj': [[policy]]
        }


class ImageToken(Token):
    def __init__(self, issuer: str, subject: str, policy: Policy = None, watermark: Watermark = None,
                 issued_at: int = None, expiration: int = None, additional_claims: dict = None, token_id: str = None):
        super().__init__(issuer, subject, [_VERB], issued_at, expiration, additional_claims, token_id)
        self.policy = policy
        self.watermark = watermark

    def to_claims(self) -> dict:
        claims = super().to_claims()

        if self.watermark:
            claims.update(self.watermark.to_claim())
        if self.policy:
            claims.update(self.policy.to_claim())

        return claims

    @classmethod
    def from_token(cls, token: Token) -> ImageToken:
        return cls(token.issuer, token.subject, None, None, token.issued_at, token.expiration, token.additional_claims,
                   token.id)
