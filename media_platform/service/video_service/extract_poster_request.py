from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.extract_poster_job import ExtractPosterSpecification
from media_platform.job.extract_poster_job_group import ExtractPosterJobGroup
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ExtractPosterRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/av/poster', ExtractPosterJobGroup)

        self.sources = []
        self.specifications = []

    def set_sources(self, sources: [Source]):
        self.sources = sources
        return self

    def add_sources(self, *sources: [Source]):
        self.sources.extend(sources)
        return self

    def set_specifications(self, specifications: [ExtractPosterSpecification]):
        self.specifications = specifications
        return self

    def add_specifications(self, *specifications: [ExtractPosterSpecification]):
        self.specifications.extend(specifications)
        return self

    def validate(self):
        [specification.validate() for specification in self.specifications]

    def execute(self) -> ExtractPosterJobGroup:
        return super().execute()

    def _params(self) -> dict:
        return {
            'sources': [source.serialize() for source in self.sources],
            'specifications': [specification.serialize() for specification in self.specifications]
        }
