from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.media_platform_request import MediaPlatformRequest


class AbortFlowRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(AbortFlowRequest, self).__init__(authenticated_http_client, 'DELETE', base_url + '/flow_control/flow/',
                                               None)

        self.id = None

        self._url = base_url + '/flow_control/flow/'

    def set_id(self, flow_id):
        # type: (str) -> AbortFlowRequest
        self.id = flow_id
        return self

    def execute(self):
        # type: () -> None
        self.url = self._url + self.id

        return super(AbortFlowRequest, self).execute()
