import time
from furl import furl
import requests
from requests import Response

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.auth.token import Token
from media_platform.service.file_service.attachment import Attachment
from media_platform.service.file_service.inline import Inline


class DownloadFileV2Request(object):
    def __init__(self, app_id, authenticator, base_url):
        # type: (str, AppAuthenticator, str) -> None

        self.path = None
        self.ttl = 600  # seconds
        self.attachment = None
        self.inline = None
        self.on_expired_redirect_to = None

        self._app_urn = 'urn:app:' + app_id
        self._url = base_url.replace('_api', '').replace('.appspot.com', '.wixmp.com')
        self._authenticator = authenticator

    def set_path(self, path):
        # type: (str) -> DownloadFileV2Request
        self.path = path
        return self

    def set_ttl(self, ttl):
        # type: (int) -> DownloadFileV2Request
        self.ttl = ttl
        return self

    def set_attachment(self, attachment):
        # type: (Attachment) -> DownloadFileV2Request
        self.attachment = attachment
        return self

    def set_inline(self, inline):
        # type: (Inline) -> DownloadFileV2Request
        self.inline = inline
        return self

    def set_on_expired_redirect_to(self, on_expired_redirect_to):
        # type: (str) -> DownloadFileV2Request
        self.on_expired_redirect_to = on_expired_redirect_to
        return self

    def url(self):
        # type: () -> str
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

    def execute(self):
        # type: () -> Response
        # http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow

        # if you don't close the response, don't come complaining about connection leakage :)
        return requests.get(self.url(), stream=True)

