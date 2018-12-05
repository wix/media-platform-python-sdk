from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.job_service.job_group_request import JobGroupRequest
from media_platform.service.job_service.job_list_request import JobListRequest
from media_platform.service.job_service.job_request import JobRequest
from media_platform.service.media_platform_service import MediaPlatformService


class JobService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None
        super(JobService, self).__init__(domain, authenticated_http_client)

    def job_request(self):
        # type: () -> JobRequest
        return JobRequest(self._authenticated_http_client, self._base_url)

    def job_group_request(self):
        # type: () -> JobGroupRequest
        return JobGroupRequest(self._authenticated_http_client, self._base_url)

    def job_list_request(self):
        # type: () -> JobListRequest
        return JobListRequest(self._authenticated_http_client, self._base_url)
