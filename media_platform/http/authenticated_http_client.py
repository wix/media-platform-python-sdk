import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from requests.structures import CaseInsensitiveDict
from urllib3 import Retry

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.http.response_processor import ResponseProcessor
from media_platform.lang.serializable import Serializable


class AuthenticatedHTTPClient(object):
    USER_AGENT = 'WixMP Python SDK 1.x'
    APPLICATION_JSON = 'application/json'
    MAX_RETRIES = 5

    RETRYABLE_CODES = [500, 503, 504, 429]
    RETRYABLE_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, authenticator):
        # type: (AppAuthenticator) -> None

        self.authenticator = authenticator

        self.session = requests.Session()

        retry = Retry(total=self.MAX_RETRIES,
                      backoff_factor=0.2,
                      status_forcelist=self.RETRYABLE_CODES,
                      method_whitelist=self.RETRYABLE_METHODS)
        self.session.mount('http://', HTTPAdapter(max_retries=retry))
        self.session.mount('https://', HTTPAdapter(max_retries=retry))

    def get(self, url, params=None, payload_type=None):
        # type: (str, dict, Serializable) -> Serializable or None

        try:
            response = self.session.get(url, params=params, headers=self._headers())
        except RetryError as e:
            raise MediaPlatformException(e)

        return ResponseProcessor.process(response, payload_type)

    def post(self, url, params=None, payload_type=None):
        # type: (str, dict, Serializable) -> Serializable or None

        try:
            response = self.session.post(url, json=params, headers=self._headers())
        except RetryError as e:
            raise MediaPlatformException(e)

        return ResponseProcessor.process(response, payload_type)

    # todo: delete
    # todo: post (form-data)

    def _headers(self):
        # type: () -> CaseInsensitiveDict

        signed_token = self.authenticator.default_signed_token()

        headers = requests.utils.default_headers()
        headers['Authorization'] = signed_token
        headers['User-Agent'] = self.USER_AGENT
        headers['Accept'] = self.APPLICATION_JSON

        return headers
