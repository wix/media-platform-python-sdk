from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.archive_service.archive_service import ArchiveService
from media_platform.service.audio_service.audio_service import AudioService
from media_platform.service.file_service.file_service import FileService
from media_platform.service.flow_control_service.flow_control_service import FlowControlService
from media_platform.service.image_service.image_service import ImageService
from media_platform.service.job_service.job_service import JobService
from media_platform.service.text_service.text_service import TextService
from media_platform.service.transcode_service.transcode_service import TranscodeService
from media_platform.service.video_service.video_service import VideoService


class MediaPlatformClient(object):
    def __init__(self, domain, app_id, shared_secret):
        # type: (str, str, str) -> None

        app_authenticator = AppAuthenticator(app_id, shared_secret)
        authenticated_http_client = AuthenticatedHTTPClient(app_authenticator)

        self.file_service = FileService(domain, authenticated_http_client, app_id, app_authenticator)
        self.job_service = JobService(domain, authenticated_http_client)
        self.video_service = VideoService(domain, authenticated_http_client)
        self.archive_service = ArchiveService(domain, authenticated_http_client, app_id, app_authenticator)
        self.transcode_service = TranscodeService(domain, authenticated_http_client)
        self.flow_control_service = FlowControlService(domain, authenticated_http_client)
        self.image_service = ImageService(domain, authenticated_http_client)
        self.audio_service = AudioService(domain, authenticated_http_client)
        self.text_service = TextService(domain, authenticated_http_client)
