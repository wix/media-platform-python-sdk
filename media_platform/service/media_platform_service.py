from media_platform.configuration.configuration import Configuration
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient


class MediaPlatformService(object):
    def __init__(self, configuration, authenticated_http_client):
        # type: (Configuration, AuthenticatedHTTPClient) -> None
        super(MediaPlatformService, self).__init__()

        self.configuration = configuration
        self.authenticated_http_client = authenticated_http_client

        self.base_url = 'https://' + self.configuration.domain + '/_api'
