from media_platform.media_platform_client import MediaPlatformClient


class Client(MediaPlatformClient):
    def __init__(self, domain, app_id, shared_secret):
        super(Client, self).__init__(domain, app_id, shared_secret)
