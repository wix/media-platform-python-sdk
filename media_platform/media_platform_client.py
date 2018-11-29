from media_platform.configuration.client_configuration import ClientConfiguration
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_service.file_service import FileService


class MediaPlatformClient(object):
    def __init__(self, domain, app_id, shared_secret):
        # type: (str, str, str) -> None
        super(MediaPlatformClient, self).__init__()

        self._configuration = ClientConfiguration(domain, app_id, shared_secret)
        self._authenticator = AppAuthenticator(self._configuration.app_id, self._configuration.shared_secret)
        self._authenticated_http_client = AuthenticatedHTTPClient(self._authenticator)

        self.file_service = FileService(self._configuration, self._authenticated_http_client)
