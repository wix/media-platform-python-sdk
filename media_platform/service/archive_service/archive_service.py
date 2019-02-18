from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.archive_service.archive_manifest_url_request import ArchiveManifestUrlRequest
from media_platform.service.archive_service.create_archive_manifest_request import CreateArchiveManifestRequest
from media_platform.service.archive_service.create_archive_request import CreateArchiveRequest
from media_platform.service.archive_service.extract_archive_request import ExtractArchiveRequest
from media_platform.service.media_platform_service import MediaPlatformService


class ArchiveService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client, app_id, app_authenticator):
        # type: (str, AuthenticatedHTTPClient, str, AppAuthenticator) -> None
        super(ArchiveService, self).__init__(domain, authenticated_http_client)

        self._app_id = app_id
        self._app_authenticator = app_authenticator

    def create_archive_request(self):
        # type: () -> CreateArchiveRequest
        return CreateArchiveRequest(self._authenticated_http_client, self._base_url)

    def create_archive_manifest_request(self):
        # type: () -> CreateArchiveManifestRequest
        return CreateArchiveManifestRequest(self._authenticated_http_client, self._base_url)

    def archive_manifest_url_request(self):
        # type: () -> ArchiveManifestUrlRequest
        return ArchiveManifestUrlRequest(self._app_id, self._app_authenticator, self._domain)

    def extract_archive_request(self):
        # type: () -> ExtractArchiveRequest
        return ExtractArchiveRequest(self._authenticated_http_client, self._base_url)
