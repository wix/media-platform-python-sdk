from media_platform.lang.serialization import Deserializable


class Rectangle(Deserializable):
    def __init__(self, x, y, width, height):
        # type: (int, int, int, int) -> None
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Rectangle
        return Rectangle(data['x'], data['y'], data['width'], data['height'])
