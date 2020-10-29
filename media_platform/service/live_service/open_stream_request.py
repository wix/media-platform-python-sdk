from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.live_service.enforced_stream_params import EnforcedStreamParams
from media_platform.service.live_service.geo_location import GeoLocation
from media_platform.service.live_service.live_stream import LiveStream
from media_platform.service.live_service.stream_dvr import StreamDVR
from media_platform.service.live_service.stream_protocol import StreamProtocol
from media_platform.service.live_service.stream_state_notification import StreamStateNotification
from media_platform.service.live_service.stream_type import StreamType
from media_platform.service.media_platform_request import MediaPlatformRequest


class OpenStreamRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/live/streams', LiveStream)
        self.protocol: StreamProtocol or None = None
        self.dvr: StreamDVR or None = None
        self.geo: GeoLocation or None = None
        self.max_stream_time_sec: int or None = None
        self.state_notification: StreamStateNotification or None = None
        self.stream_type: StreamType = StreamType.event
        self.connect_timeout: int or None = None
        self.reconnect_timeout: int or None = None
        self.enforced_stream_params: EnforcedStreamParams or None = None

    def set_protocol(self, protocol: StreamProtocol) -> OpenStreamRequest:
        self.protocol = protocol
        return self

    def set_dvr(self, dvr: StreamDVR) -> OpenStreamRequest:
        self.dvr = dvr
        return self

    def set_geo(self, geo: GeoLocation) -> OpenStreamRequest:
        self.geo = geo
        return self

    def set_max_stream_time_sec(self, max_stream_time_sec) -> OpenStreamRequest:
        self.max_stream_time_sec = max_stream_time_sec
        return self

    def set_state_notification(self, state_notification: StreamStateNotification) -> OpenStreamRequest:
        self.state_notification = state_notification
        return self

    def set_stream_type(self, stream_type: StreamType) -> OpenStreamRequest:
        self.stream_type = stream_type
        return self

    def set_connect_timeout(self, connect_timeout: int) -> OpenStreamRequest:
        self.connect_timeout = connect_timeout
        return self

    def set_reconnect_timeout(self, reconnect_timeout: int) -> OpenStreamRequest:
        self.reconnect_timeout = reconnect_timeout
        return self

    def set_enforced_stream_params(self, enforced_stream_params: EnforcedStreamParams) -> OpenStreamRequest:
        self.enforced_stream_params = enforced_stream_params
        return self

    def _params(self) -> dict:
        return {
            'protocol': self.protocol,
            'maxStreamingSec': self.max_stream_time_sec,
            'streamType': self.stream_type,
            'connectTimeout': self.connect_timeout,
            'reconnectTimeout': self.reconnect_timeout,
            'enforcedStreamParams': self.enforced_stream_params.serialize() if self.enforced_stream_params else None,
            'stateNotification': self.state_notification.serialize() if self.state_notification else None,
            'dvr': self.dvr.serialize() if self.dvr else None,
            'geo': self.geo.serialize() if self.geo else None
        }
