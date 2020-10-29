from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.job.transcode_job_group import TranscodeJobGroup
from media_platform.service.callback import Callback
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class TranscodeRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/av/transcode', TranscodeJobGroup)

        self.sources = []
        self.specifications = []
        self.callback = None

    def set_sources(self, sources: [Source]):
        self.sources = sources
        return self

    def add_sources(self, *sources: [Source]):
        self.sources.extend(sources)
        return self

    def set_specifications(self, specifications: [TranscodeSpecification]):
        self.specifications = specifications
        return self

    def add_specifications(self, *specifications: [TranscodeSpecification]):
        self.specifications.extend(specifications)
        return self

    def set_callback(self, callback: Callback):
        self.callback = callback
        return self

    def validate(self):
        [specification.validate() for specification in self.specifications]

    def execute(self) -> TranscodeJobGroup:
        return super().execute()

    def _params(self) -> dict:
        return {
            'sources': [source.serialize() for source in self.sources],
            'specifications': [specification.serialize() for specification in self.specifications],
            'jobCallback': self.callback.serialize() if self.callback else None
        }
