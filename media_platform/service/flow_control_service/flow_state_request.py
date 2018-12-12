from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.flow_control_service.flow_state import FlowState
from media_platform.service.media_platform_request import MediaPlatformRequest


class FlowStateRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(FlowStateRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/flow_control/flow/',
                                               FlowState)

        self.id = None

        self._url = base_url + '/flow_control/flow/'

    def set_id(self, flow_id):
        # type: (str) -> FlowStateRequest
        self.id = flow_id
        return self

    def execute(self):
        # type: () -> FlowState
        self.url = self._url + self.id

        return super(FlowStateRequest, self).execute()
