from typing import Type

from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.lang.serialization import Deserializable


class MediaPlatformRequest(object):
    def __init__(self, authenticated_http_client, method, url, payload_type=None):
        # type: (AuthenticatedHTTPClient, str, str, Type[Deserializable]) -> None
        self.authenticated_http_client = authenticated_http_client

        self.method = method
        self.url = url
        self.payload_type = payload_type

    def execute(self):
        # type: () -> Deserializable or None

        self.validate()

        if self.method == 'GET':
            return self.authenticated_http_client.get(self.url, self._params(), self.payload_type)

        if self.method == 'POST':
            return self.authenticated_http_client.post(self.url, self._params(), self.payload_type)

        raise NotImplementedError('method not supported')

    # override for request pre-flight check
    def validate(self):
        pass

    # noinspection PyMethodMayBeStatic
    def _params(self):
        # type: () -> dict
        return {}
