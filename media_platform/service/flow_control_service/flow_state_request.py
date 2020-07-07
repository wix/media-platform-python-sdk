from __future__ import annotations

from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.flow_control_service.flow_state import FlowState
from media_platform.service.media_platform_request import MediaPlatformRequest


class FlowStateRequest(MediaPlatformRequest):
    flow_id: str

    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super(FlowStateRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/flow_control/flow/',
                                               FlowState)
        self._url = base_url + '/flow_control/flow/'

    def set_id(self, flow_id: str) -> FlowStateRequest:
        self.flow_id = flow_id
        return self

    def execute(self) -> FlowState:
        self.url = self._url + self.flow_id

        return super(FlowStateRequest, self).execute()
