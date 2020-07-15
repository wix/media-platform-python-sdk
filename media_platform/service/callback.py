from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class Callback(Serializable, Deserializable):
    def __init__(self, url: str, attachment: dict = None, headers: dict = None, passthrough: bool = False):
        self.url = url
        self.attachment = attachment
        self.headers = headers
        self.passthrough = passthrough

    @classmethod
    def deserialize(cls, data: dict) -> Callback:
        return cls(data['url'], data.get('attachment'), data.get('headers'), data.get('passthrough', False))

    def serialize(self) -> dict:
        return {
            'url': self.url,
            'attachment': self.attachment,
            'headers': self.headers,
            'passthrough': self.passthrough
        }
