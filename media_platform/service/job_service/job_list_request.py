from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.job_service.job_list import JobList
from media_platform.service.list_request import _ListRequest


class JobListRequest(_ListRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(JobListRequest, self).__init__(authenticated_http_client, base_url + '/jobs', JobList)

        self.issuer = None
        self.type = None
        self.status = None
        self.group_id = None
        self.file_id = None
        self.path = None

    def set_issuer(self, issuer):
        # type: (str) -> JobListRequest
        self.issuer = issuer
        return self

    def set_type(self, job_type):
        # type: (str) -> JobListRequest
        self.type = job_type
        return self

    def set_status(self, status):
        # type: (str) -> JobListRequest
        self.status = status
        return self

    def set_path(self, path):
        # type: (str) -> JobListRequest
        self.path = path
        return self

    def execute(self):
        # type: () -> JobList
        return super(JobListRequest, self).execute()

    def _params(self):
        # type: () -> dict
        params = super(JobListRequest, self)._params()

        if self.issuer:
            params['issuer'] = self.issuer

        if self.type:
            params['type'] = self.type

        if self.status:
            params['status'] = self.status

        if self.group_id:
            params['groupId'] = self.group_id

        if self.file_id:
            params['fileId'] = self.file_id

        if self.path:
            params['path'] = self.path

        return params
