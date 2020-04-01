from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from typing import Dict

from media_platform.service.live_service.enforced_stream_params import EnforcedStreamParams
from media_platform.service.live_service.geo_location import GeoLocation
from media_platform.service.live_service.live_stream import LiveStream
from media_platform.service.live_service.stream_dvr import StreamDVR
from media_platform.service.live_service.stream_protocol import StreamProtocol
from media_platform.service.live_service.stream_state_notification import StreamStateNotification
from media_platform.service.live_service.stream_type import StreamType
from media_platform.service.media_platform_request import MediaPlatformRequest


class OpenStreamRequest(MediaPlatformRequest):

    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(OpenStreamRequest, self).__init__(authenticated_http_client, 'POST', base_url + '/live/streams',
                                                LiveStream)

        self.protocol = None  # type: StreamProtocol
        self.dvr = None  # type: StreamDVR
        self.geo = None  # type: GeoLocation
        self.max_stream_time_sec = None  # type: int
        self.state_notification = None  # type: StreamStateNotification or None
        self.stream_type = StreamType.event  # type: StreamType
        self.connect_timeout = None  # type: int
        self.reconnect_timeout = None  # type: int
        self.enforced_stream_params = None  # type: EnforcedStreamParams

    def set_protocol(self, protocol):
        # type: (StreamProtocol) -> OpenStreamRequest
        self.protocol = protocol
        return self

    def set_dvr(self, dvr):
        # type: (StreamDVR) -> OpenStreamRequest
        self.dvr = dvr
        return self

    def set_geo(self, geo):
        self.geo = geo
        return self

    def set_max_stream_time_sec(self, max_stream_time_sec):
        self.max_stream_time_sec = max_stream_time_sec
        return self

    def set_state_notification(self, state_notification):
        self.state_notification = state_notification
        return self

    def set_stream_type(self, stream_type):
        # type: (StreamType) -> OpenStreamRequest
        self.stream_type = stream_type
        return self

    def set_connect_timeout(self, connect_timeout):
        self.connect_timeout = connect_timeout
        return self

    def set_reconnect_timeout(self, reconnect_timeout):
        self.reconnect_timeout = reconnect_timeout
        return self

    def set_enforced_stream_params(self, enforced_stream_params):
        self.enforced_stream_params = enforced_stream_params
        return self

    def _params(self):
        # type: () -> Dict

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
