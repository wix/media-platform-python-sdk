from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.scan_file_job_group import ScanFileJobGroup
from media_platform.job.scan_file_job import ScanFileSpecification
from media_platform.service.callback import Callback
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ScanFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/security/av/scan', ScanFileJobGroup)

        self.source = None
        self.callback = None

    def set_source(self, source: Source) -> ScanFileRequest:
        self.source = source
        return self

    def set_callback(self, callback: Callback):
        self.callback = callback
        return self

    def _params(self) -> dict:
        return {
            'source': self.source.serialize(),
            'jobCallback': self.callback.serialize() if self.callback else None,
            'specification': None,
        }
