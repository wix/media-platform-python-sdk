from __future__ import annotations

import time
from furl import furl
import requests

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.auth.token import Token
from media_platform.service.file_service.attachment import Attachment
from media_platform.service.file_service.inline import Inline


class DownloadFileRequest:
    def __init__(self, app_id: str, authenticator: AppAuthenticator, base_url: str):
        self._app_urn = 'urn:app:' + app_id
        self._url = base_url.replace('_api', '').replace('.appspot.com', '.wixmp.com')
        self._authenticator = authenticator

        self.path = None
        self.ttl = 600  # seconds
        self.attachment = None
        self.inline = None
        self.on_expired_redirect_to = None

    def set_path(self, path: str) -> DownloadFileRequest:
        self.path = path
        return self

    def set_ttl(self, ttl: int) -> DownloadFileRequest:
        self.ttl = ttl
        return self

    def set_attachment(self, attachment: Attachment) -> DownloadFileRequest:
        self.attachment = attachment
        return self

    def set_inline(self, inline: Inline) -> DownloadFileRequest:
        self.inline = inline
        return self

    def set_on_expired_redirect_to(self, on_expired_redirect_to: str) -> DownloadFileRequest:
        self.on_expired_redirect_to = on_expired_redirect_to
        return self

    def url(self) -> str:
        additional_claims = {
            'obj': [[{'path': self.path}]]
        }
        if self.on_expired_redirect_to:
            additional_claims['red'] = self.on_expired_redirect_to

        token = Token(
            self._app_urn,
            self._app_urn,
            ['urn:service:file.download'],
            expiration=int(time.time()) + self.ttl,
            additional_claims=additional_claims
        )

        signed_token = self._authenticator.sign_token(token)

        url = furl(self._url).add(path=self.path).add(query_params={'token': signed_token})

        if self.attachment and self.inline:
            raise ValueError('Can\'t set both attachment and inline')

        if self.attachment:
            url.add(query_params={'filename': self.attachment.file_name})
        elif self.inline:
            url.add(query_params={'filename': self.inline.file_name})
            url.add(query_params={'inline': ''})

        return url.url

    def execute(self) -> requests.Response:
        # http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow

        # if you don't close the response, don't come complaining about connection leakage :)
        return requests.get(self.url(), stream=True)
