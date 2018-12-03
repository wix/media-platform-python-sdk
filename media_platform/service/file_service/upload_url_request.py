from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import ACL, FileDescriptor, FileMimeType
from media_platform.service.file_service.upload_url import UploadUrl
from media_platform.service.media_platform_request import MediaPlatformRequest


class UploadUrlRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(UploadUrlRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/upload/url', UploadUrl)

        self.path = None
        self.mime_type = FileMimeType.defualt
        self.acl = ACL.public

    def set_path(self, path):
        # type: (str) -> UploadUrlRequest
        self.path = path
        return self

    def set_mime_type(self, mime_type):
        # type: (str) -> UploadUrlRequest
        self.mime_type = mime_type
        return self

    def set_acl(self, acl):
        # type: (ACL) -> UploadUrlRequest
        self.acl = acl
        return self

    def execute(self):
        # type: () -> UploadUrl
        return super(UploadUrlRequest, self).execute()

    def validate(self):
        FileDescriptor.path_validator(self.path)
        FileDescriptor.acl_validator(self.acl)

    def _params(self):
        return {
            'path': self.path,
            'mimeType': self.mime_type,
            'acl': self.acl,
        }
