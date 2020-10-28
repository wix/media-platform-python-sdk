from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.job import Job
from media_platform.service.media_platform_request import MediaPlatformRequest

# noinspection PyProtectedMember
from media_platform.job.job_deserializer import _JobDeserializer


class JobRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'GET', base_url + '/jobs/', _JobDeserializer)
        self.job_id = None

        self._url = base_url + '/jobs/'

    def set_id(self, job_id: str) -> JobRequest:
        self.job_id = job_id
        return self

    def execute(self) -> Job:
        self.url = self._url + self.job_id

        return super().execute()
