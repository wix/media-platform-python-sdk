from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.image_operation_job import ImageOperationSpecification
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ImageOperationRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/images/operations', FileDescriptor)
        self.source = None
        self.specification = None

    def set_source(self, source: Source) -> ImageOperationRequest:
        self.source = source
        return self

    def set_specification(self, specification: ImageOperationSpecification) -> ImageOperationRequest:
        self.specification = specification
        return self

    def _params(self) -> dict:
        return {
            'source': self.source.serialize(),
            'specification': self.specification.serialize(),
        }

    def execute(self) -> FileDescriptor:
        return super().execute()
