from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.extract_archive.extract_archive_job import ExtractArchiveJob
from media_platform.job.extract_archive.extraction_report import ExtractionReport
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ExtractArchiveRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/archive/extract', ExtractArchiveJob)
        self.source = None
        self.destination = None
        self.report = None
        self.callback = None

    def set_source(self, source: Source) -> ExtractArchiveRequest:
        self.source = source
        return self

    def set_destination(self, destination: Destination) -> ExtractArchiveRequest:
        self.destination = destination
        return self

    def set_report(self, extraction_report: ExtractionReport) -> ExtractArchiveRequest:
        self.report = extraction_report
        return self

    def set_callback(self, callback: Callback) -> ExtractArchiveRequest:
        self.callback = callback
        return self

    def execute(self) -> ExtractArchiveJob:
        return super().execute()

    def _params(self) -> dict:
        return {
            'source': self.source.serialize(),
            'destination': self.destination.serialize(),
            'extractedFilesReport': self.report.serialize() if self.report else None,
            'jobCallback': self.callback.serialize() if self.callback else None
        }
