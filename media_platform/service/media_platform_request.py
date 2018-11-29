from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient


class MediaPlatformRequest(object):
    def __init__(self,  authenticated_http_client, method, url, payload_type=None):
        # type: (AuthenticatedHTTPClient, str, str, object) -> None
        super(MediaPlatformRequest, self).__init__()
        self.authenticated_http_client = authenticated_http_client

        self.method = method
        self.url = url

        self.payload_type = payload_type

    def execute(self):

        self.validate()

        if self.method == 'GET':
            return self.authenticated_http_client.get(self.url, self._param(), self.payload_type)

    # override for request pre-flight check
    def validate(self):
        pass

    # noinspection PyMethodMayBeStatic
    def _param(self):
        # type: () -> dict
        return {}
