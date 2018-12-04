from media_platform.lang.serialization import Deserializable


class Color(Deserializable):
    def __init__(self, r, g, b, pixel_fraction, score):
        # type: (int, int, int, float, float) -> None
        super(Color, self).__init__()
        self.r = r
        self.g = g
        self.b = b
        self.pixel_fraction = pixel_fraction
        self.score = score

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Color
        return Color(data['r'], data['g'], data['b'], data['pixelFraction'], data['score'])
