from media_platform.lang.serialization import Serializable, Deserializable


class Lyrics(Serializable, Deserializable):
    def __init__(self, text, language=None, description=None):
        # type: (str, str, str) -> None
        self.description = description
        self.language = language
        self.text = text

        # backwards compatibility
        self.lang = self.language

    def serialize(self):
        # type: () -> dict
        return {
            'text': self.text,
            'description': self.description,
            'language': self.language,

            # backwards compatibility
            'lang': self.language,
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Lyrics
        return cls(data['text'], data.get('language') or data.get('lang'), data.get('description'))
