from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.image_operation_job import ImageOperationSpecification
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ImageOperationRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(ImageOperationRequest, self).__init__(authenticated_http_client, 'POST', base_url + '/images/operations',
                                                    FileDescriptor)

        self.source = None
        self.specification = None

    def set_source(self, source):
        # type: (Source) -> ImageOperationRequest
        self.source = source
        return self

    def set_specification(self, specification):
        # type: (ImageOperationSpecification) -> ImageOperationRequest
        self.specification = specification
        return self

    def _params(self):
        return {
            'source': self.source.serialize(),
            'specification': self.specification.serialize(),
        }

    def execute(self):
        # type: () -> FileDescriptor
        return super(ImageOperationRequest, self).execute()
