import requests

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

        signed_token = self.authenticator.default_signed_token()

        response = requests.get(url, params, headers={
            'Authorization': signed_token
        })

        data = response.json()

        return RestResult.deserialize(data)
