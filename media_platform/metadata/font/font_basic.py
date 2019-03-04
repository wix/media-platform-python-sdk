from media_platform.lang.serialization import Deserializable


class FontBasic(Deserializable):
    def __init__(self, font_type):
        # type: (str) -> None
        super(FontBasic, self).__init__()
        self.font_type = font_type

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FontBasic
        return FontBasic(data['fontType'])
