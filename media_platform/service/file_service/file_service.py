from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_service.copy_file_request import CopyFileRequest
from media_platform.service.file_service.create_file_request import CreateFileRequest
from media_platform.service.file_service.delete_file_request import DeleteFileRequest
from media_platform.service.file_service.download_file_request import DownloadFileRequest
from media_platform.service.file_service.get_file_request import GetFileRequest
from media_platform.service.file_service.import_file_request import ImportFileRequest
from media_platform.service.file_service.upload_file_request import UploadFileRequest
from media_platform.service.file_service.upload_url_request import UploadUrlRequest
from media_platform.service.media_platform_service import MediaPlatformService


class FileService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client, app_id, app_authenticator):
        # type: (str, AuthenticatedHTTPClient, str, AppAuthenticator) -> None
        super(FileService, self).__init__(domain, authenticated_http_client)

        self._app_id = app_id
        self._app_authenticator = app_authenticator

    def get_file_request(self):
        # type: () -> GetFileRequest
        return GetFileRequest(self._authenticated_http_client, self._base_url)

    def create_file_request(self):
        # type: () -> CreateFileRequest
        return CreateFileRequest(self._authenticated_http_client, self._base_url)

    def upload_url_request(self):
        # type: () -> UploadUrlRequest
        return UploadUrlRequest(self._authenticated_http_client, self._base_url)

    def upload_file_request(self):
        # type: () -> UploadFileRequest
        return UploadFileRequest(self._authenticated_http_client, self._base_url)

    def import_file_request(self):
        # type: () -> ImportFileRequest
        return ImportFileRequest(self._authenticated_http_client, self._base_url)

    def delete_file_request(self):
        # type: () -> DeleteFileRequest
        return DeleteFileRequest(self._authenticated_http_client, self._base_url)

    def copy_file_request(self):
        # type: () -> CopyFileRequest
        return CopyFileRequest(self._authenticated_http_client, self._base_url)

    def download_file_request(self):
        # type: () -> DownloadFileRequest
        return DownloadFileRequest(self._app_id, self._app_authenticator, self._base_url)
