from media_platform.lang.serialization import Serializable, Deserializable


class Callback(Serializable, Deserializable):
    def __init__(self, url, attachment=None, headers=None):
        # type: (str, dict, dict) -> None

        self.url = url
        self.attachment = attachment
        self.headers = headers

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Callback
        return cls(data['url'], data.get('attachment'), data.get('headers'))

    def serialize(self):
        # type: () -> dict
        return {
            'url': self.url,
            'attachment': self.attachment,
            'headers': self.headers
        }
