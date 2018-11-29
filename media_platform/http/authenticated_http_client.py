import requests
from requests import Response
from requests.structures import CaseInsensitiveDict

from media_platform.auth.authenticator import Authenticator
from media_platform.service.rest_result import RestResult


class AuthenticatedHTTPClient(object):

    USER_AGENT = 'WixMP Python SDK 1.x'

    def __init__(self, authenticator):
        # type: (Authenticator) -> None
        super(AuthenticatedHTTPClient, self).__init__()

        self.authenticator = authenticator

    def get(self, url, params=None):
        # type: (str, dict) -> RestResult

        response = requests.get(url, params, headers=self._headers())

        return self._handle_response(response)

    def _headers(self):
        # type: () -> CaseInsensitiveDict

        signed_token = self.authenticator.default_signed_token()

        headers = requests.utils.default_headers()
        headers['Authorization'] = signed_token
        headers['User-Agent'] = self.USER_AGENT
        headers['Accept'] = 'application/json'

        return headers

    def _handle_response(self, response):
        # type: (Response) -> RestResult

        # todo: error handling

        data = response.json()
        return RestResult.deserialize(data)
