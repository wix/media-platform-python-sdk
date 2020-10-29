from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.flow_control_service.abort_flow_request import AbortFlowRequest
from media_platform.service.flow_control_service.flow_invocation_request import FlowInvocationRequest
from media_platform.service.flow_control_service.flow_state_request import FlowStateRequest
from media_platform.service.media_platform_service import MediaPlatformService


class FlowControlService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient):
        super().__init__(domain, authenticated_http_client)

    def invoke_flow_request(self) -> FlowInvocationRequest:
        return FlowInvocationRequest(self._authenticated_http_client, self._base_url)

    def flow_state_request(self) -> FlowStateRequest:
        return FlowStateRequest(self._authenticated_http_client, self._base_url)

    def abort_flow_request(self) -> AbortFlowRequest:
        return AbortFlowRequest(self._authenticated_http_client, self._base_url)
