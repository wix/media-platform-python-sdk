from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileType
from media_platform.service.file_service.file_list import FileList
from media_platform.service.media_platform_request import MediaPlatformRequest


class OrderBy(object):
    name = 'name'
    date_updated = 'dateUpdated'


class OrderDirection(object):
    ascending = 'acs'
    descending = 'des'


class FileListRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(FileListRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/files/ls_dir', FileList)

        self.path = None

        self.next_page_token = None
        self.page_size = 20
        self.order_by = OrderBy.date_updated
        self.order_direction = OrderDirection.descending
        self.recursive = False
        self.type = FileType.file

    def set_path(self, path):
        # type: (str) -> FileListRequest
        self.path = path
        return self

    def set_next_page_token(self, next_page_token):
        # type: (str) -> FileListRequest
        self.next_page_token = next_page_token
        return self

    def set_page_size(self, page_size):
        # type: (int) -> FileListRequest
        self.page_size = page_size
        return self

    def set_order_by(self, order_by):
        # type: (str) -> FileListRequest
        self.order_by = order_by
        return self

    def set_order_direction(self, order_direction):
        # type: (str) -> FileListRequest
        self.order_direction = order_direction
        return self

    def set_recursive(self, recursive):
        # type: (bool) -> FileListRequest
        self.recursive = recursive
        return self

    def set_type(self, file_type):
        # type: (str) -> FileListRequest
        self.type = file_type
        return self

    def execute(self):
        # type: () -> FileList
        return super(FileListRequest, self).execute()

    def _params(self):
        # type: () -> dict

        params = {
            'path': self.path
        }

        if self.next_page_token:
            params['nextPageToken'] = self.next_page_token

        if self.page_size:
            params['pageSize'] = self.page_size

        if self.order_by:
            params['orderBy'] = self.order_by

        if self.order_direction:
            params['orderDirection'] = self.order_direction

        if self.recursive:
            params['r'] = self.recursive

        if self.type:
            params['type'] = self.type

        return params
