from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.import_file_job import ImportFileJob
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.file_service.external_authorization import ExternalAuthorization
from media_platform.service.media_platform_request import MediaPlatformRequest


class ImportFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/import/file', ImportFileJob)
        self.source_url = None
        self.external_authorization = None
        self.destination = None
        self.job_callback = None

    def set_source_url(self, source_url: str) -> ImportFileRequest:
        self.source_url = source_url
        return self

    def set_external_authorization(self, external_authorization: ExternalAuthorization) -> ImportFileRequest:
        self.external_authorization = external_authorization
        return self

    def set_destination(self, destination: Destination) -> ImportFileRequest:
        self.destination = destination
        return self

    def set_job_callback(self, job_callback: Callback) -> ImportFileRequest:
        self.job_callback = job_callback
        return self

    def execute(self) -> ImportFileJob:
        return super().execute()

    def _params(self) -> dict:
        return {
            'sourceUrl': self.source_url,
            'externalAuthorization': self.external_authorization.serialize() if self.external_authorization else None,
            'destination': self.destination.serialize(),
            'jobCallback': self.job_callback.serialize() if self.job_callback else None
        }
