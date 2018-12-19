from media_platform.service.file_descriptor import FileDescriptor
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification
from media_platform.service.media_platform_request import MediaPlatformRequest


class ReplaceExtraMetadataRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(ReplaceExtraMetadataRequest, self).__init__(authenticated_http_client, 'PUT',
                                                          base_url + '/av/extra-metadata', FileDescriptor)
        self.specification = None  # type: ReplaceAudioExtraMetadataSpecification

    def set_specification(self, specification):
        # type: (ReplaceAudioExtraMetadataSpecification) -> ReplaceExtraMetadataRequest
        self.specification = specification
        return self

    def execute(self):
        # type: () -> FileDescriptor
        return super(ReplaceExtraMetadataRequest, self).execute()

    def _params(self):
        return {
            'specification': self.specification.serialize()
        }
