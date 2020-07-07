from __future__ import annotations

from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.metadata.file_metadata import FileMetadata
from media_platform.service.media_platform_request import MediaPlatformRequest
# noinspection PyProtectedMember
from media_platform.metadata.file_metadata_deserializer import _FileMetadataDeserializer


class Detection:
    transparency = 'transparency'
    valid_values = [transparency]

    @classmethod
    def validate(cls, value):
        if value not in cls.valid_values:
            raise ValueError('Must be one of: ' + ','.join(cls.valid_values))


class ExtractMetadataRequest(MediaPlatformRequest):
    path: str
    detections: [Detection] = []

    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super(ExtractMetadataRequest, self).__init__(authenticated_http_client, 'GET',
                                                     base_url + '/files/metadata/extract', _FileMetadataDeserializer)

    def set_path(self, path: str) -> ExtractMetadataRequest:
        self.path = path
        return self

    def set_detections(self, detections: [Detection]) -> ExtractMetadataRequest:
        self.detections = detections
        return self

    def add_detection(self, *detection: [Detection]) -> ExtractMetadataRequest:
        self.detections.extend(detection)
        return self

    def execute(self) -> FileMetadata:
        return super(ExtractMetadataRequest, self).execute()

    def _params(self) -> dict:
        return {
            'path': self.path,
            'detections': ','.join(self.detections)
        }
