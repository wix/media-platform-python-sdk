import requests

from media_platform.auth.authenticator import Authenticator


class AuthenticatedHTTPClient(object):

    USER_AGENT = 'WixMP Python SDK 1.x'

    def __init__(self, authenticator):
        # type: (Authenticator) -> None
        super(AuthenticatedHTTPClient, self).__init__()

        self.authenticator = authenticator

    def get(self, url):

        signed_token = self.authenticator.default_signed_token()

        requests.get(url, headers={
            'Authorization': signed_token
        })
