from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient


class MediaPlatformService(object):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None

        self._domain = domain

        self._authenticated_http_client = authenticated_http_client

        self._base_url = 'https://' + domain + '/_api'
