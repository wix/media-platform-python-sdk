from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.extract_poster_job import ExtractPosterSpecification
from media_platform.job.extract_poster_job_group import ExtractPosterJobGroup
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class ExtractPosterRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(ExtractPosterRequest, self).__init__(authenticated_http_client, 'POST', base_url + '/av/poster',
                                                   ExtractPosterJobGroup)

        self.sources = []
        self.specifications = []

    def set_sources(self, sources):
        # type: ([Source]) -> ExtractPosterRequest
        self.sources = sources
        return self

    def add_sources(self, *sources):
        # type: ([Source]) -> ExtractPosterRequest
        self.sources.extend(sources)
        return self

    def set_specifications(self, specifications):
        # type: ([ExtractPosterSpecification]) -> ExtractPosterRequest
        self.specifications = specifications
        return self

    def add_specifications(self, *specifications):
        # type: ([ExtractPosterSpecification]) -> ExtractPosterRequest
        self.specifications.extend(specifications)
        return self

    def validate(self):
        [specification.validate() for specification in self.specifications]

    def execute(self):
        # type: () -> ExtractPosterJobGroup
        return super(ExtractPosterRequest, self).execute()

    def _params(self):
        return {
            'sources': [source.serialize() for source in self.sources],
            'specifications': [specification.serialize() for specification in self.specifications]
        }
