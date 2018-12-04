from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class CopyFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(CopyFileRequest, self).__init__(authenticated_http_client, 'POST', base_url + '/copy/file',
                                              FileDescriptor)

        self.source = None
        self.destination = None

    def set_source(self, source):
        # type: (Source) -> CopyFileRequest
        self.source = source
        return self

    def set_destination(self, destination):
        # type: (Destination) -> CopyFileRequest
        self.destination = destination
        return self

    def _params(self):
        return {
            'source': self.source.serialize(),
            'destination': self.destination.serialize(),
        }
