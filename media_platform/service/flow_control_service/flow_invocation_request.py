from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.flow_control_service.flow import Flow
from media_platform.service.flow_control_service.flow_state import FlowState
from media_platform.service.flow_control_service.invocation import Invocation
from media_platform.service.media_platform_request import MediaPlatformRequest


class FlowInvocationRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(FlowInvocationRequest, self).__init__(authenticated_http_client, 'POST', base_url + '/flow_control/flow',
                                                    FlowState)

        self.invocation = None  # type: Invocation
        self.flow = None  # type: Flow

    def set_invocation(self, invocation):
        # type: (Invocation) -> FlowInvocationRequest
        self.invocation = invocation
        return self

    def set_flow(self, flow):
        # type: (Flow) -> FlowInvocationRequest
        self.flow = flow
        return self

    def validate(self):
        self.flow.validate()
        self._validate_entry_points()

    def execute(self):
        # type: () -> FlowState
        return super(FlowInvocationRequest, self).execute()

    def _params(self):
        return {
            'invocation': self.invocation.serialize(),
            'flow': self.flow.serialize(),
        }

    def _validate_entry_points(self):
        invalid_entry_points = [e for e in self.invocation.entry_points if e not in self.flow.components]
        if invalid_entry_points:
            raise ValueError('entry points not defined in components: %s' % invalid_entry_points)
