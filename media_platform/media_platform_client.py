from media_platform.configuration.configuration import Configuration


class MediaPlatformClient(object):
    def __init__(self, domain, app_id, shared_secret):
        super(MediaPlatformClient, self).__init__()

        self.configuration = Configuration(domain, app_id, shared_secret)
