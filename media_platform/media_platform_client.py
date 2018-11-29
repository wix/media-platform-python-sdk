from media_platform.configuration.client_configuration import ClientConfiguration


class MediaPlatformClient(object):
    def __init__(self, domain, app_id, shared_secret):
        # type: (str, str, str) -> None

        self.configuration = ClientConfiguration(domain, app_id, shared_secret)
