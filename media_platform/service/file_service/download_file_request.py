import time
import requests
from requests import Response

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.auth.token import Token
from media_platform.service.file_service.attachment import Attachment


class DownloadFileRequest(object):
    def __init__(self, app_id, authenticator, base_url):
        # type: (str, AppAuthenticator, str) -> None

        self.path = None
        self.ttl = 600  # seconds
        self.attachment = None
        self.on_expired_redirect_to = None

        self._app_urn = 'urn:app:' + app_id
        self._url = base_url + '/download/file'
        self._authenticator = authenticator

    def set_path(self, path):
        # type: (str) -> DownloadFileRequest
        self.path = path
        return self

    def set_ttl(self, ttl):
        # type: (int) -> DownloadFileRequest
        self.ttl = ttl
        return self

    def set_attachment(self, attachment):
        # type: (Attachment) -> DownloadFileRequest
        self.attachment = attachment
        return self

    def set_on_expired_redirect_to(self, on_expired_redirect_to):
        # type: (str) -> DownloadFileRequest
        self.on_expired_redirect_to = on_expired_redirect_to
        return self

    def url(self):
        # type: () -> str

        payload = {'path': self.path}
        if self.on_expired_redirect_to:
            payload['onExpireRedirectTo'] = self.on_expired_redirect_to
        if self.attachment:
            payload['attachment'] = self.attachment.serialize()

        token = Token(
            self._app_urn,
            self._app_urn,
            ['urn:service:file.download'],
            int(time.time()) - 10,
            int(time.time()) + self.ttl,
            {'payload': payload}
        )

        signed_token = self._authenticator.sign_token(token)

        return self._url + '?downloadToken=' + signed_token

    def execute(self):
        # type: () -> Response
        # http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow

        # if you don't close the response, don't come complaining about connection leakage :)
        return requests.get(self._url, stream=True)
