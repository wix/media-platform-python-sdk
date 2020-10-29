from media_platform.lang.serialization import Deserializable, Serializable


class StreamStateNotification(Serializable, Deserializable):
    def __init__(self, callback_url: str, custom_payload: dict = None):
        self.callback_url = callback_url
        self.custom_payload = custom_payload or {}

    @classmethod
    def deserialize(cls, data: dict):
        return StreamStateNotification(data.get('notifyUrl') or data['callbackUrl'], data.get('customPayload'))

    def serialize(self) -> dict:
        return {
            'callbackUrl': self.callback_url,
            'customPayload': self.custom_payload
        }
