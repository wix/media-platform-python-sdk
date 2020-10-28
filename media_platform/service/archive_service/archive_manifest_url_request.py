from __future__ import annotations

import time

import requests
from requests import Response

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.auth.token import Token


class ArchiveManifestUrlRequest:
    def __init__(self, app_id: str, authenticator: AppAuthenticator, domain: str):
        self.path = None
        self.ttl = None  # seconds

        self._app_urn = 'urn:app:' + app_id
        self._authenticator = authenticator

        self._url = '//archive-' + domain.replace('.appspot.com', '.wixmp.com')

    def set_path(self, path: str) -> ArchiveManifestUrlRequest:
        self.path = path
        return self

    def set_ttl(self, ttl: int) -> ArchiveManifestUrlRequest:
        self.ttl = ttl
        return self

    def url(self) -> str:
        url = self._url + self.path

        if self.ttl:
            auth_token = self._get_token()
            url += '?auth=' + auth_token

        return url

    def execute(self) -> Response:
        # http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow

        # if you don't close the response, don't come complaining about connection leakage :)
        return requests.get('https:' + self.url(), stream=True)

    def _get_token(self) -> str:
        objects = [
            [{
                'path': self.path
            }]
        ]

        token = Token(
            self._app_urn,
            self._app_urn,
            ['urn:service:file.download'],
            int(time.time()) - 10,
            int(time.time()) + self.ttl,
            {'obj': objects}
        )

        return self._authenticator.sign_token(token)
