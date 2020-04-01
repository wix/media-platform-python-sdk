class StreamStateNotification(object):
    def __init__(self, callback_url, custom_payload=None):
        # type: (str, dict) -> None

        self.callback_url = callback_url
        self.custom_payload = custom_payload or {}

    @staticmethod
    def deserialize(data):
        # type: (dict) -> StreamStateNotification
        return StreamStateNotification(data.get('notifyUrl') or data['callbackUrl'], data.get('customPayload'))

    def serialize(self):
        # type: () -> dict

        return {
            'callbackUrl': self.callback_url,
            'customPayload': self.custom_payload
        }
