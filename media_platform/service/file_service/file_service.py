from media_platform.configuration.configuration import Configuration
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_service.create_file_request import CreateFileRequest
from media_platform.service.file_service.get_file_request import GetFileRequest
from media_platform.service.media_platform_service import MediaPlatformService


class FileService(MediaPlatformService):
    def __init__(self, configuration, authenticated_http_client):
        # type: (Configuration, AuthenticatedHTTPClient) -> None
        super(FileService, self).__init__(configuration, authenticated_http_client)

    def get_file_request(self):
        return GetFileRequest(self.authenticated_http_client, self.configuration.base_url)

    def create_file_request(self):
        return CreateFileRequest(self.authenticated_http_client, self.configuration.base_url)
