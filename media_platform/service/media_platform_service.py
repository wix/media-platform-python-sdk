from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient


class MediaPlatformService:
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient):
        self._domain = domain

        self._authenticated_http_client = authenticated_http_client

        self._base_url = 'https://' + domain + '/_api'
