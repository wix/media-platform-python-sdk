from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.file_service.create_file_request import CreateFileRequest
from media_platform.service.file_service.create_files_response import _CreateFilesResponse
from media_platform.service.media_platform_request import MediaPlatformRequest


class CreateFilesRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/files', FileDescriptor)
        self.file_requests = []

    def execute(self) -> Deserializable or None:
        # TODO: Replace with single request once server supports that
        file_descriptors = [self.authenticated_http_client.post(self.url, f._params(), self.response_payload_type) for f
                            in self.file_requests]

        return _CreateFilesResponse(file_descriptors)

    def set_file_requests(self, file_requests: [CreateFileRequest]) -> CreateFilesRequest:
        self.file_requests = file_requests
        return self

    def add_file(self, *file_request: [CreateFileRequest]) -> CreateFilesRequest:
        self.file_requests.extend(file_request)
        return self

    def _params(self):
        return {
            'files': [file_request._params() for file_request in self.file_requests]
        }
