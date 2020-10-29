from __future__ import annotations

from typing import Type

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.lang.serialization import Deserializable
from media_platform.service.media_platform_request import MediaPlatformRequest


class OrderBy:
    name = 'name'
    date_updated = 'dateUpdated'


class OrderDirection:
    ascending = 'acs'
    descending = 'des'


class _ListRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, url: str,
                 payload_type: Type[Deserializable]):
        super().__init__(authenticated_http_client, 'GET', url, payload_type)
        self.next_page_token = None
        self.page_size = 20
        self.order_by = OrderBy.date_updated
        self.order_direction = OrderDirection.descending

    def set_next_page_token(self, next_page_token: str):
        self.next_page_token = next_page_token
        return self

    def set_page_size(self, page_size: int):
        self.page_size = page_size
        return self

    def set_order_by(self, order_by: OrderBy):
        self.order_by = order_by
        return self

    def set_order_direction(self, order_direction: OrderDirection):
        self.order_direction = order_direction
        return self

    def _params(self) -> dict:
        params = {}

        if self.next_page_token:
            params['nextPageToken'] = self.next_page_token

        if self.page_size:
            params['pageSize'] = self.page_size

        if self.order_by:
            params['orderBy'] = self.order_by

        if self.order_direction:
            params['orderDirection'] = self.order_direction

        return params
