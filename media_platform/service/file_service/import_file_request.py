from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.import_file_job import ImportFileJob
from media_platform.lang.serialization import Serializable
from media_platform.service.destination import Destination
from media_platform.service.media_platform_request import MediaPlatformRequest


class ExternalAuthorization(Serializable):
    def __init__(self, headers):
        # type: (dict) -> None
        super(ExternalAuthorization, self).__init__()

        self.headers = headers

    def serialize(self):
        return {
            'headers': self.headers
        }


class ImportFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(ImportFileRequest, self).__init__(authenticated_http_client, 'POST', base_url + '/import/file',
                                                ImportFileJob)

        self.source_url = None
        self.external_authorization = None  # type: ExternalAuthorization
        self.destination = None  # type: Destination

    def set_source_url(self, source_url):
        # type: (str) -> ImportFileRequest
        self.source_url = source_url
        return self

    def set_external_authorization(self, external_authorization):
        # type: (ExternalAuthorization) -> ImportFileRequest
        self.external_authorization = external_authorization
        return self

    def set_destination(self, destination):
        # type: (Destination) -> ImportFileRequest
        self.destination = destination
        return self

    def execute(self):
        # type: () -> ImportFileJob
        return super(ImportFileRequest, self).execute()

    def _params(self):
        return {
            'sourceUrl': self.source_url,
            'externalAuthorization': self.external_authorization.serialize() if self.external_authorization else None,
            'destination': self.destination.serialize()
        }
