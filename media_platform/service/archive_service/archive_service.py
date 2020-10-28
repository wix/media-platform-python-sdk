from __future__ import annotations

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.archive_service.archive_manifest_url_request import ArchiveManifestUrlRequest
from media_platform.service.archive_service.create_archive_manifest_request import CreateArchiveManifestRequest
from media_platform.service.archive_service.create_archive_request import CreateArchiveRequest
from media_platform.service.archive_service.extract_archive_request import ExtractArchiveRequest
from media_platform.service.media_platform_service import MediaPlatformService


class ArchiveService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient, app_id: str,
                 app_authenticator: AppAuthenticator):
        super().__init__(domain, authenticated_http_client)
        self._app_id = app_id
        self._app_authenticator = app_authenticator

    def create_archive_request(self) -> CreateArchiveRequest:
        return CreateArchiveRequest(self._authenticated_http_client, self._base_url)

    def create_archive_manifest_request(self) -> CreateArchiveManifestRequest:
        return CreateArchiveManifestRequest(self._authenticated_http_client, self._base_url)

    def archive_manifest_url_request(self) -> ArchiveManifestUrlRequest:
        return ArchiveManifestUrlRequest(self._app_id, self._app_authenticator, self._domain)

    def extract_archive_request(self) -> ExtractArchiveRequest:
        return ExtractArchiveRequest(self._authenticated_http_client, self._base_url)
