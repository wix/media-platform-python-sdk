from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.metadata.audio_file_metadata import AudioFileMetadata
from media_platform.service.media_platform_request import MediaPlatformRequest


class ExtractMetadataRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(ExtractMetadataRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/audio/metadata', AudioFileMetadata)

        self.path = None

    def set_path(self, path):
        # type: (str) -> ExtractMetadataRequest
        self.path = path
        return self

    def execute(self):
        # type: () -> AudioFileMetadata
        return super(ExtractMetadataRequest, self).execute()

    def _params(self):
        # type: () -> dict
        return {
            'path': self.path
        }
