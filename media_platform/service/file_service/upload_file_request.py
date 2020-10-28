from __future__ import annotations

import json

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.callback import Callback
from media_platform.service.file_descriptor import ACL, FileDescriptor, FileMimeType
from media_platform.service.file_service.upload_configuration_request import UploadConfigurationRequest
from media_platform.service.lifecycle import Lifecycle
from media_platform.service.media_platform_request import MediaPlatformRequest


class UploadFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url, FileDescriptor)

        self.path = None
        self.mime_type = FileMimeType.defualt
        self.acl = ACL.public
        self.size = None
        self.lifecycle = None
        self.callback = None
        self.bucket = None
        self.response_processor = None
        self.filename = 'filename'
        self.content = None

    def set_path(self, path: str) -> UploadFileRequest:
        self.path = path
        return self

    def set_mime_type(self, mime_type: str) -> UploadFileRequest:
        self.mime_type = mime_type
        return self

    def set_acl(self, acl: ACL) -> UploadFileRequest:
        self.acl = acl
        return self

    def set_size(self, size: int) -> UploadFileRequest:
        self.size = size
        return self

    def set_lifecycle(self, lifecycle: Lifecycle) -> UploadFileRequest:
        self.lifecycle = lifecycle
        return self

    def set_callback(self, callback: Callback) -> UploadFileRequest:
        self.callback = callback
        return self

    def set_bucket(self, bucket: str) -> UploadFileRequest:
        self.bucket = bucket
        return self

    def override_response_processor(self, response_processor: callable) -> UploadFileRequest:
        self.response_processor = response_processor
        return self

    def set_filename(self, filename: str) -> UploadFileRequest:
        self.filename = filename
        return self

    def set_content(self, content: str) -> UploadFileRequest:
        self.content = content
        return self

    def validate(self):
        FileDescriptor.path_validator(self.path)
        FileDescriptor.acl_validator(self.acl)

    def execute(self) -> FileDescriptor:
        self.validate()

        config = UploadConfigurationRequest(self.authenticated_http_client, self.url).set_path(
            self.path
        ).set_acl(self.acl).set_mime_type(self.mime_type).set_callback(self.callback).set_size(
            self.size
        ).set_bucket(self.bucket).execute()

        params = self._params()
        return self.authenticated_http_client.post_data(config.upload_url, self.content, self.mime_type, params,
                                                        FileDescriptor, self.filename, self.response_processor)

    def _params(self) -> dict:
        return {
            'lifecycle': json.dumps(self.lifecycle.serialize()) if self.lifecycle else None,
        }
