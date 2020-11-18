from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.media_platform_service import MediaPlatformService
from media_platform.service.scanner_service.scan_file_request import ScanFileRequest


class ScannerService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient):
        super(ScannerService, self).__init__(domain, authenticated_http_client)

    def scan_file_request(self) -> ScanFileRequest:
        return ScanFileRequest(self._authenticated_http_client, self._base_url)
