from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileType
from media_platform.service.file_service.file_list import FileList
from media_platform.service.list_request import _ListRequest, OrderBy, OrderDirection


class FileListRequest(_ListRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, base_url + '/files/ls_dir', FileList)
        self.path = None
        self.recursive = False
        self.type = FileType.file

    def set_path(self, path: str) -> FileListRequest:
        self.path = path
        return self

    def set_recursive(self, recursive: bool) -> FileListRequest:
        self.recursive = recursive
        return self

    def set_type(self, file_type: FileType) -> FileListRequest:
        self.type = file_type
        return self

    def set_next_page_token(self, next_page_token: str) -> FileListRequest:
        return super().set_next_page_token(next_page_token)

    def set_page_size(self, page_size: int) -> FileListRequest:
        return super().set_page_size(page_size)

    def set_order_by(self, order_by: OrderBy) -> FileListRequest:
        return super().set_order_by(order_by)

    def set_order_direction(self, order_direction: OrderDirection) -> FileListRequest:
        return super().set_order_direction(order_direction)

    def execute(self) -> FileList:
        return super().execute()

    def _params(self) -> dict:
        params = super()._params()

        params['path'] = self.path

        if self.recursive:
            params['r'] = self.recursive

        if self.type:
            params['type'] = self.type

        return params
