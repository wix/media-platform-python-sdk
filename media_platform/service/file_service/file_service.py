from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
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
from media_platform.service.file_service.upload_file_v2_request import UploadFileV2Request
from media_platform.service.file_service.upload_url_request import UploadUrlRequest
from media_platform.service.media_platform_service import MediaPlatformService


class FileService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client, app_id, app_authenticator):
        # type: (str, AuthenticatedHTTPClient, str, AppAuthenticator) -> None
        super(FileService, self).__init__(domain, authenticated_http_client)

        self._app_id = app_id
        self._app_authenticator = app_authenticator

    def file_request(self):
        # type: () -> FileRequest
        return FileRequest(self._authenticated_http_client, self._base_url)

    def create_file_request(self):
        # type: () -> CreateFileRequest
        return CreateFileRequest(self._authenticated_http_client, self._base_url)

    def update_file_request(self):
        # type: () -> UpdateFileRequest
        return UpdateFileRequest(self._authenticated_http_client, self._base_url)

    def create_files_request(self):
        # type: () -> CreateFilesRequest
        return CreateFilesRequest(self._authenticated_http_client, self._base_url)

    def upload_url_request(self):
        # type: () -> UploadUrlRequest
        return UploadUrlRequest(self._authenticated_http_client, self._base_url)

    def upload_file_request(self):
        # type: () -> UploadFileRequest
        return UploadFileRequest(self._authenticated_http_client, self._base_url)

    def upload_configuration_request(self):
        # type: () -> UploadConfigurationRequest
        return UploadConfigurationRequest(self._authenticated_http_client, self._base_url)

    def upload_file_v2_request(self):
        # type: () -> UploadFileV2Request
        return UploadFileV2Request(self._authenticated_http_client, self._base_url)

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

    def file_list_request(self):
        # type: () -> FileListRequest
        return FileListRequest(self._authenticated_http_client, self._base_url)

    def file_metadata_request(self):
        # type: () -> FileMetadataRequest
        return FileMetadataRequest(self._authenticated_http_client, self._base_url)

    def extract_metadata_request(self):
        # type: () -> ExtractMetadataRequest
        return ExtractMetadataRequest(self._authenticated_http_client, self._base_url)
