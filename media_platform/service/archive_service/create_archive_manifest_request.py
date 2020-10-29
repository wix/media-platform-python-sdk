from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.create_archive_job import ArchiveSource
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ZipAlgorithm:
    # compresses the objects
    zip = 'zip'
    # copies them as is, for already compressed files such as mp3, mp4, etc.
    store = 'store'

    @classmethod
    def has_value(cls, value):
        return value in [ZipAlgorithm.store, ZipAlgorithm.zip]


class CreateArchiveManifestRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/archive/create/manifest', FileDescriptor)
        self.name = None
        self.sources = []
        self.destination = None
        self.algorithm = 'zip'

    def set_sources(self, sources: [Source or ArchiveSource]) -> CreateArchiveManifestRequest:
        self.sources = sources
        return self

    def add_sources(self, *sources: [Source or ArchiveSource]) -> CreateArchiveManifestRequest:
        self.sources.extend(sources)
        return self

    def set_destination(self, destination: Destination) -> CreateArchiveManifestRequest:
        self.destination = destination
        return self

    def set_name(self, name: str) -> CreateArchiveManifestRequest:
        self.name = name
        return self

    def set_algorithm(self, algorithm: ZipAlgorithm) -> CreateArchiveManifestRequest:
        self.algorithm = algorithm
        return self

    def execute(self) -> FileDescriptor:
        return super().execute()

    def _params(self) -> dict:
        return {
            'name': self.name,
            'sources': [source.serialize() for source in self.sources if source],
            'destination': self.destination.serialize(),
            'algorithm': self.algorithm
        }
