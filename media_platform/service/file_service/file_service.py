from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_service.create_file_request import CreateFileRequest
from media_platform.service.file_service.delete_file_request import DeleteFileRequest
from media_platform.service.file_service.get_file_request import GetFileRequest
from media_platform.service.file_service.import_file_request import ImportFileRequest
from media_platform.service.file_service.upload_file_request import UploadFileRequest
from media_platform.service.file_service.upload_url_request import UploadUrlRequest
from media_platform.service.media_platform_service import MediaPlatformService


class FileService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None
        super(FileService, self).__init__(domain, authenticated_http_client)

    def get_file_request(self):
        # type: () -> GetFileRequest
        return GetFileRequest(self.authenticated_http_client, self.base_url)

    def create_file_request(self):
        # type: () -> CreateFileRequest
        return CreateFileRequest(self.authenticated_http_client, self.base_url)

    def upload_url_request(self):
        # type: () -> UploadUrlRequest
        return UploadUrlRequest(self.authenticated_http_client, self.base_url)

    def upload_file_request(self):
        # type: () -> UploadFileRequest
        return UploadFileRequest(self.authenticated_http_client, self.base_url)

    def import_file_request(self):
        # type: () -> ImportFileRequest
        return ImportFileRequest(self.authenticated_http_client, self.base_url)

    def delete_file_request(self):
        # type: () -> DeleteFileRequest
        return DeleteFileRequest(self.authenticated_http_client, self.base_url)
