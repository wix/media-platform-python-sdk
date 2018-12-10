from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.flow_control_service.flow_invocation_request import FlowInvocationRequest
from media_platform.service.media_platform_service import MediaPlatformService


class FlowControlService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None
        super(FlowControlService, self).__init__(domain, authenticated_http_client)

    def invoke_flow_request(self):
        # type: () -> FlowInvocationRequest
        return FlowInvocationRequest(self._authenticated_http_client, self._base_url)
