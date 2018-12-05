from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileType
from media_platform.service.file_service.file_list import FileList
from media_platform.service.list_request import _ListRequest


class FileListRequest(_ListRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(FileListRequest, self).__init__(authenticated_http_client, base_url + '/files/ls_dir', FileList)

        self.path = None
        self.recursive = False
        self.type = FileType.file

    def set_path(self, path):
        # type: (str) -> FileListRequest
        self.path = path
        return self

    def set_recursive(self, recursive):
        # type: (bool) -> FileListRequest
        self.recursive = recursive
        return self

    def set_type(self, file_type):
        # type: (str) -> FileListRequest
        self.type = file_type
        return self

    def set_next_page_token(self, next_page_token):
        # type: (str) -> FileListRequest
        return super(FileListRequest, self).set_next_page_token(next_page_token)

    def set_page_size(self, page_size):
        # type: (int) -> FileListRequest
        return super(FileListRequest, self).set_page_size(page_size)

    def set_order_by(self, order_by):
        # type: (str) -> FileListRequest
        return super(FileListRequest, self).set_order_by(order_by)

    def set_order_direction(self, order_direction):
        # type: (str) -> FileListRequest
        return super(FileListRequest, self).set_order_direction(order_direction)

    def execute(self):
        # type: () -> FileList
        return super(FileListRequest, self).execute()

    def _params(self):

        params = super(FileListRequest, self)._params()

        params['path'] = self.path

        if self.recursive:
            params['r'] = self.recursive

        if self.type:
            params['type'] = self.type

        return params
