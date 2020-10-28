from __future__ import annotations

from typing import Type

from media_platform.service.source import Source
from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification, \
    ReplaceExtraMetadataJob
from media_platform.service.media_platform_request import MediaPlatformRequest


class ReplaceExtraMetadataBaseRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str, verb: str,
                 response_type: Type[Deserializable]):
        super().__init__(authenticated_http_client, verb, base_url + '/av/extra-metadata', response_type)
        self.source = None
        self.specification = None

    def set_specification(self,
                          specification: ReplaceAudioExtraMetadataSpecification) -> ReplaceExtraMetadataBaseRequest:
        self.specification = specification
        return self

    def set_source(self, source: Source) -> ReplaceExtraMetadataBaseRequest:
        self.source = source
        return self

    def _params(self) -> dict:
        return {
            'source': self.source.serialize(),
            'specification': self.specification.serialize()
        }


class ReplaceExtraMetadataSyncRequest(ReplaceExtraMetadataBaseRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, base_url, 'PUT', FileDescriptor)


class ReplaceExtraMetadataAsyncRequest(ReplaceExtraMetadataBaseRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, base_url, 'POST', ReplaceExtraMetadataJob)
