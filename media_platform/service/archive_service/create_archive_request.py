from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.create_archive_job import ArchiveSource, CreateArchiveJob, ArchiveType
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class CreateArchiveRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/archive/create', CreateArchiveJob)
        self.sources = []
        self.destination = None
        self.archive_type = 'zip'
        self.callback = None

    def set_sources(self, sources: [Source or ArchiveSource]) -> CreateArchiveRequest:
        self.sources = sources
        return self

    def add_sources(self, *sources: [Source or ArchiveSource]) -> CreateArchiveRequest:
        self.sources.extend(sources)
        return self

    def set_destination(self, destination: Destination) -> CreateArchiveRequest:
        self.destination = destination
        return self

    def set_archive_type(self, archive_type: ArchiveType) -> CreateArchiveRequest:
        self.archive_type = archive_type
        return self

    def set_callback(self, callback: Callback) -> CreateArchiveRequest:
        self.callback = callback
        return self

    def execute(self) -> CreateArchiveJob:
        return super().execute()

    def _params(self) -> dict:
        return {
            'sources': [source.serialize() for source in self.sources if source],
            'destination': self.destination.serialize(),
            'archiveType': self.archive_type,
            'jobCallback': self.callback.serialize() if self.callback else None
        }
