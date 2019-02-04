from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.callback import Callback
from media_platform.service.file_descriptor import ACL
from media_platform.service.file_service.upload_configuration import UploadConfiguration
from media_platform.service.media_platform_request import MediaPlatformRequest


class UploadConfigurationRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(UploadConfigurationRequest, self).__init__(authenticated_http_client, 'POST',
                                                         base_url + '/v2/upload/configuration', UploadConfiguration)
        self.path = None
        self.bucket = None
        self.mime_type = None
        self.acl = None
        self.size = None
        self.callback = None

    def set_path(self, path):
        # type: (str) -> UploadConfigurationRequest
        self.path = path
        return self

    def set_bucket(self, bucket):
        # type: (str) -> UploadConfigurationRequest
        self.bucket = bucket
        return self

    def set_mime_type(self, mime_type):
        # type: (str) -> UploadConfigurationRequest
        self.mime_type = mime_type
        return self

    def set_acl(self, acl):
        # type: (ACL) -> UploadConfigurationRequest
        self.acl = acl
        return self

    def set_size(self, size):
        # type: (int) -> UploadConfigurationRequest
        self.size = size
        return self

    def set_callback(self, callback):
        # type: (Callback) -> UploadConfigurationRequest
        self.callback = callback
        return self

    def execute(self):
        # type: () -> UploadConfiguration
        return super(UploadConfigurationRequest, self).execute()

    def validate(self):
        # todo
        super(UploadConfigurationRequest, self).validate()

    def _params(self):
        # type: () -> dict
        return {
            'path': self.path,
            'bucket': self.bucket,
            'mimeType': self.mime_type,
            'size': self.size,
            'acl': self.acl,
            'callback':  self.callback.serialize() if self.callback else None
        }
