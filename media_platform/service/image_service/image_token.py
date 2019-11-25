from media_platform.auth.token import Token

_VERB = 'urn:service:image.operations'


class Gravity(object):
    center = 'center'
    north = "north"
    north_west = "north-west"
    west = "west"
    south_west = "south-west"
    south = "south"
    south_east = "south-east"
    east = "east"
    north_east = "north-east"


class Watermark(object):
    def __init__(self, path, opacity=50, proportions=0.25, gravity=Gravity.center):
        # type: (str, int, float, Gravity) -> None
        super(Watermark, self).__init__()
        self.path = path
        self.opacity = opacity
        self.proportions = proportions
        self.gravity = gravity

    def to_claim(self):
        # type: () -> dict
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


class Policy(object):
    def __init__(self, path, max_width=None, max_height=None):
        # type: (str, int, int) -> None
        super(Policy, self).__init__()
        self.path = path
        self.max_width = max_width
        self.max_height = max_height

    def to_claim(self):
        # type: () -> dict
        policy = {}
        if self.path:
            policy['path'] = self.path
        if self.max_height:
            policy['height'] = '<=%s' % self.max_height
        if self.max_width:
            policy['width'] = '<=%s' % self.max_width

        return {
            'obj': [[policy]]
        }


class ImageToken(Token):
    def __init__(self, issuer, subject, policy=None, watermark=None, issued_at=None, expiration=None,
                 additional_claims=None, token_id=None):
        super(ImageToken, self).__init__(issuer, subject, [_VERB], issued_at, expiration, additional_claims, token_id)
        self.policy = policy
        self.watermark = watermark

    def to_claims(self):
        # type: () -> dict
        claims = super(ImageToken, self).to_claims()

        if self.watermark:
            claims.update(self.watermark.to_claim())
        if self.policy:
            claims.update(self.policy.to_claim())

        return claims

    @classmethod
    def from_token(cls, token):
        # type: (Token) -> ImageToken
        return cls(token.issuer, token.subject, None, None, token.issued_at, token.expiration, token.additional_claims,
                   token.id)
