from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.job import Job
from media_platform.service.media_platform_request import MediaPlatformRequest

# noinspection PyProtectedMember
from media_platform.job.job_deserializer import _JobDeserializer


class JobRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(JobRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/jobs/', _JobDeserializer)

        self.id = None

        self._url = base_url + '/jobs/'

    def set_id(self, job_id):
        # type: (str) -> JobRequest
        self.id = job_id
        return self

    def execute(self):
        # type: () -> Job

        self.url = self._url + self.id

        return super(JobRequest, self).execute()
