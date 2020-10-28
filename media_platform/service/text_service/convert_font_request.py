from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.convert_font_job import ConvertFontSpecification
from media_platform.job.convert_font_job_group import ConvertFontJobGroup
from media_platform.service.callback import Callback
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ConvertFontRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/fonts/convert', ConvertFontJobGroup)

        self.source = None
        self.specification = None
        self.callback = None

    def set_source(self, source: Source):
        self.source = source
        return self

    def set_specification(self, specification: ConvertFontSpecification):
        self.specification = specification
        return self

    def set_callback(self, callback: Callback):
        self.callback = callback
        return self

    def validate(self):
        self.specification.validate()

    def execute(self) -> ConvertFontJobGroup:
        return super().execute()

    def _params(self) -> dict:
        return {
            'source': self.source.serialize(),
            'specification': self.specification.serialize(),
            'jobCallback': self.callback.serialize() if self.callback else None
        }
