import time

import requests
from requests import Response

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.auth.token import Token


class ArchiveManifestUrlRequest(object):
    def __init__(self, app_id, authenticator, domain):
        # type: (str, AppAuthenticator, str) -> None
        self.path = None
        self.ttl = None  # seconds
        # self.attachment = None
        # self.on_expired_redirect_to = None

        self._app_urn = 'urn:app:' + app_id
        self._authenticator = authenticator

        self._url = '//archive-' + domain.replace('.appspot.com', '.wixmp.com')

    def set_path(self, path):
        # type: (str) -> ArchiveManifestUrlRequest
        self.path = path
        return self

    def set_ttl(self, ttl):
        # type: (int) -> ArchiveManifestUrlRequest
        self.ttl = ttl
        return self

    # todo
    # def set_attachment(self, attachment):
    #     # type: (Attachment) -> ArchiveManifestUrlRequest
    #     self.attachment = attachment
    #     return self
    #
    # def set_on_expired_redirect_to(self, on_expired_redirect_to):
    #     # type: (str) -> ArchiveManifestUrlRequest
    #     self.on_expired_redirect_to = on_expired_redirect_to
    #     return self

    def url(self):
        # type: () -> str
        url = self._url + self.path

        if self.ttl:
            auth_token = self._get_token()
            url += '?auth=' + auth_token

        return url

    def execute(self):
        # type: () -> Response
        # http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow

        # if you don't close the response, don't come complaining about connection leakage :)
        return requests.get('https:' + self.url(), stream=True)

    def _get_token(self):
        # type: () -> str
        objects = [
            [{
                'path': self.path
            }]
        ]

        # payload = {}
        # if self.on_expired_redirect_to:
        #     payload['onExpireRedirectTo'] = self.on_expired_redirect_to
        # if self.attachment:
        #     payload['attachment'] = self.attachment.serialize()

        token = Token(
            self._app_urn,
            self._app_urn,
            ['urn:service:file.download'],
            int(time.time()) - 10,
            int(time.time()) + self.ttl,
            {'obj': objects}
        )

        return self._authenticator.sign_token(token)
