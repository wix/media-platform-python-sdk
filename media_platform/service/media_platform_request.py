from abc import ABC

from typing import Type

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.lang.serialization import Deserializable


class MediaPlatformRequest(ABC):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, method: str, url: str,
                 response_payload_type: Type[Deserializable] = None):
        self.authenticated_http_client = authenticated_http_client
        self.method = method
        self.url = url
        self.response_payload_type = response_payload_type

    def execute(self) -> Deserializable or None:
        self.validate()

        if self.method == 'GET':
            return self.authenticated_http_client.get(self.url, self._params(), self.response_payload_type)
        elif self.method == 'POST':
            return self.authenticated_http_client.post(self.url, self._params(), self.response_payload_type)
        elif self.method == 'PUT':
            return self.authenticated_http_client.put(self.url, self._params(), self.response_payload_type)
        elif self.method == 'DELETE':
            return self.authenticated_http_client.delete(self.url, self._params(), self.response_payload_type)
        else:
            raise ValueError('method not supported %s' % self.method)

    # override for request pre-flight check
    def validate(self):
        pass

    # noinspection PyMethodMayBeStatic
    def _params(self) -> dict:
        return {}
