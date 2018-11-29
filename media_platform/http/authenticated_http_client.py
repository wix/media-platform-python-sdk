import requests
from requests import Response
from requests.adapters import HTTPAdapter
from requests.structures import CaseInsensitiveDict
from urllib3 import Retry

from media_platform.auth.authenticator import Authenticator
from media_platform.exception.forbidden_exception import ForbiddenException
from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.exception.not_found_exception import NotFoundException
from media_platform.exception.unauthorized_exception import UnauthorizedException
from media_platform.lang.serializable import Serializable
from media_platform.service.rest_result import RestResult


class AuthenticatedHTTPClient(object):
    USER_AGENT = 'WixMP Python SDK 1.x'
    APPLICATION_JSON = 'application/json'
    MAX_RETRIES = 5

    RETRYABLE_CODES = [500, 503, 504, 429]
    RETRYABLE_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, authenticator):
        # type: (Authenticator) -> None
        super(AuthenticatedHTTPClient, self).__init__()

        self.authenticator = authenticator

        self.session = requests.Session()

        retry = Retry(total=self.MAX_RETRIES,
                      backoff_factor=0.5,
                      status_forcelist=self.RETRYABLE_CODES,
                      method_whitelist=self.RETRYABLE_METHODS)
        self.session.mount('http://', HTTPAdapter(max_retries=retry))
        self.session.mount('https://', HTTPAdapter(max_retries=retry))

    def get(self, url, params=None, payload_type=None):
        # type: (str, dict, Serializable) -> Serializable or None

        response = self.session.get(url, params=params, headers=self._headers())

        return self._handle_response(response, payload_type)

    def _headers(self):
        # type: () -> CaseInsensitiveDict

        signed_token = self.authenticator.default_signed_token()

        headers = requests.utils.default_headers()
        headers['Authorization'] = signed_token
        headers['User-Agent'] = self.USER_AGENT
        headers['Accept'] = self.APPLICATION_JSON

        return headers

    def _handle_response(self, response, payload_type=None):
        # type: (Response, Serializable) -> Serializable or None

        if response.status_code == 401:
            raise UnauthorizedException()

        if response.status_code == 403:
            raise ForbiddenException()

        if response.status_code == 404:
            raise NotFoundException()

        if response.status_code < 200 or response.status_code > 299:
            raise MediaPlatformException()

        try:
            rest_result = RestResult.deserialize(response.json())
        except ValueError as e:
            raise MediaPlatformException(e)

        if rest_result.code != 0:
            # todo: code -> exception mapper (Alon, have fun :))
            raise MediaPlatformException()

        if payload_type:
            return payload_type.deserialize(rest_result.payload)
        else:
            return None
