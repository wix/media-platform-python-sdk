import json

from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.callback import Callback
from media_platform.service.file_descriptor import ACL, FileDescriptor, FileMimeType
from media_platform.service.file_service.upload_file_response import _UploadFileResponse
from media_platform.service.file_service.upload_url_request import UploadUrlRequest
from media_platform.service.lifecycle import Lifecycle
from media_platform.service.media_platform_request import MediaPlatformRequest


class UploadFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(UploadFileRequest, self).__init__(authenticated_http_client, 'POST', base_url, FileDescriptor)

        self.path = None
        self.mime_type = FileMimeType.defualt
        self.acl = ACL.public
        self.lifecycle = None
        self.callback = None

        self.content = None

    def set_path(self, path):
        # type: (str) -> UploadFileRequest
        self.path = path
        return self

    def set_mime_type(self, mime_type):
        # type: (str) -> UploadFileRequest
        self.mime_type = mime_type
        return self

    def set_acl(self, acl):
        # type: (ACL) -> UploadFileRequest
        self.acl = acl
        return self

    def set_lifecycle(self, lifecycle):
        # type: (Lifecycle) -> UploadFileRequest
        self.lifecycle = lifecycle
        return self

    def set_callback(self, callback):
        # type: (Callback) -> UploadFileRequest
        self.callback = callback
        return self

    def set_content(self, content):
        self.content = content
        return self

    def validate(self):
        FileDescriptor.path_validator(self.path)
        FileDescriptor.acl_validator(self.acl)

    def execute(self):
        # type: () -> FileDescriptor
        self.validate()

        upload_url = UploadUrlRequest(self.authenticated_http_client, self.url).set_path(self.path).set_acl(
            self.acl
        ).set_mime_type(self.mime_type).execute()

        params = self._params()
        params.update({
            'uploadToken': upload_url.upload_token
        })

        response = self.authenticated_http_client.post_data(upload_url.upload_url, self.content, self.mime_type, params,
                                                            _UploadFileResponse)

        return response.file_descriptors[0]

    def _params(self):
        # type: () -> dict
        return {
            'path': self.path,
            'mimeType': self.mime_type,
            'acl': self.acl,
            'lifecycle': json.dumps(self.lifecycle.serialize()) if self.lifecycle else None,
            'callback': json.dumps(self.callback.serialize()) if self.callback else None,
        }
