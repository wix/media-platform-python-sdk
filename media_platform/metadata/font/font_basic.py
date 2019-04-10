from media_platform.lang.serialization import Deserializable


class FontBasic(Deserializable):
    def __init__(self, font_type=None, name=None, family=None):
        # type: (str, str, str) -> None
        super(FontBasic, self).__init__()
        self.font_type = font_type
        self.name = name
        self.family = family

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FontBasic
        return FontBasic(data['fontType'], data.get('name'), data.get('family'))
