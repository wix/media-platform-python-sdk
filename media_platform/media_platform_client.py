from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_service.file_service import FileService
from media_platform.service.job_service.job_service import JobService
from media_platform.service.video_service.video_service import VideoService


class MediaPlatformClient(object):
    def __init__(self, domain, app_id, shared_secret):
        # type: (str, str, str) -> None

        app_authenticator = AppAuthenticator(app_id, shared_secret)
        authenticated_http_client = AuthenticatedHTTPClient(app_authenticator)

        self.file_service = FileService(domain, authenticated_http_client, app_id, app_authenticator)
        self.job_service = JobService(domain, authenticated_http_client)
        self.video_service = VideoService(domain, authenticated_http_client)
