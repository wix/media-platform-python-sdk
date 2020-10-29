from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_service.copy_file_request import CopyFileRequest
from media_platform.service.file_service.create_file_request import CreateFileRequest
from media_platform.service.file_service.create_files_request import CreateFilesRequest
from media_platform.service.file_service.delete_file_request import DeleteFileRequest
from media_platform.service.file_service.download_file_request import DownloadFileRequest
from media_platform.service.file_service.extract_metadata_request import ExtractMetadataRequest
from media_platform.service.file_service.file_list_request import FileListRequest
from media_platform.service.file_service.file_metadata_request import FileMetadataRequest
from media_platform.service.file_service.file_request import FileRequest
from media_platform.service.file_service.import_file_request import ImportFileRequest
from media_platform.service.file_service.update_file_request import UpdateFileRequest
from media_platform.service.file_service.upload_configuration_request import UploadConfigurationRequest
from media_platform.service.file_service.upload_file_request import UploadFileRequest
from media_platform.service.media_platform_service import MediaPlatformService


class FileService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient, app_id: str,
                 app_authenticator: AppAuthenticator):
        super().__init__(domain, authenticated_http_client)
        self._app_id = app_id
        self._app_authenticator = app_authenticator

    def file_request(self) -> FileRequest:
        return FileRequest(self._authenticated_http_client, self._base_url)

    def create_file_request(self) -> CreateFileRequest:
        return CreateFileRequest(self._authenticated_http_client, self._base_url)

    def update_file_request(self) -> UpdateFileRequest:
        return UpdateFileRequest(self._authenticated_http_client, self._base_url)

    def create_files_request(self) -> CreateFilesRequest:
        return CreateFilesRequest(self._authenticated_http_client, self._base_url)

    def upload_configuration_request(self) -> UploadConfigurationRequest:
        return UploadConfigurationRequest(self._authenticated_http_client, self._base_url)

    def upload_file_request(self) -> UploadFileRequest:
        return UploadFileRequest(self._authenticated_http_client, self._base_url)

    def import_file_request(self) -> ImportFileRequest:
        return ImportFileRequest(self._authenticated_http_client, self._base_url)

    def delete_file_request(self) -> DeleteFileRequest:
        return DeleteFileRequest(self._authenticated_http_client, self._base_url)

    def copy_file_request(self) -> CopyFileRequest:
        return CopyFileRequest(self._authenticated_http_client, self._base_url)

    def download_file_request(self) -> DownloadFileRequest:
        return DownloadFileRequest(self._app_id, self._app_authenticator, self._base_url)

    def file_list_request(self) -> FileListRequest:
        return FileListRequest(self._authenticated_http_client, self._base_url)

    def file_metadata_request(self) -> FileMetadataRequest:
        return FileMetadataRequest(self._authenticated_http_client, self._base_url)

    def extract_metadata_request(self) -> ExtractMetadataRequest:
        return ExtractMetadataRequest(self._authenticated_http_client, self._base_url)
