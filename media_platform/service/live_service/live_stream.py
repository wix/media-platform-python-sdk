from __future__ import annotations

from datetime import datetime

from media_platform.lang import datetime_serialization
from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.live_service.enforced_stream_params import EnforcedStreamParams, \
    StreamParamsOutOfRangeErrorInfo
from media_platform.service.live_service.geo_location import GeoLocation
from media_platform.service.live_service.stream_dvr import StreamDVR
from media_platform.service.live_service.stream_error_code import StreamErrorCode
from media_platform.service.live_service.stream_error_info import StreamErrorInfo
from media_platform.service.live_service.stream_playback import StreamPlayback
from media_platform.service.live_service.stream_protocol import StreamProtocol
from media_platform.service.live_service.stream_publisher_endpoint import StreamPublishEndpoint
from media_platform.service.live_service.stream_state import StreamState
from media_platform.service.live_service.stream_state_notification import StreamStateNotification
from media_platform.service.live_service.stream_type import StreamType


class LiveStream(Serializable, Deserializable):
    def __init__(self, project_id: str, streamer_id: str, stream_id: str, playbacks: [StreamPlayback],
                 publish_endpoint: StreamPublishEndpoint or None, dvr: StreamDVR or None,
                 state: StreamState, duration: int, max_publish_duration: int, date_created: datetime,
                 date_updated: datetime,
                 state_notification: StreamStateNotification or None, stream_type: StreamType, success: bool,
                 error_message: str,
                 connect_timeout_secs: int, reconnect_timeout_secs: int, probe_result: dict, protocol: StreamProtocol,
                 enforced_stream_params: EnforcedStreamParams, publisher_geo: GeoLocation, error_code: StreamErrorCode,
                 error_info: StreamErrorInfo):
        self.stream_type = stream_type
        self.project_id = project_id
        self.streamer_id = streamer_id
        self.id = stream_id
        self.playback = playbacks or []
        self.publish_endpoint = publish_endpoint
        self.dvr = dvr
        self.state = state
        self.duration = duration
        self.max_publish_duration = max_publish_duration
        self.state_notification = state_notification
        self.date_created = date_created or datetime.utcnow()
        self.date_updated = date_updated or datetime.utcnow()
        self.success = success
        self.error_message = error_message
        self.connect_timeout_secs = connect_timeout_secs
        self.reconnect_timeout_secs = reconnect_timeout_secs
        self.probe_result = probe_result
        self.protocol = protocol
        self.enforced_stream_params = enforced_stream_params
        self.publisher_geo = publisher_geo
        self.error_code = error_code
        self.error_info = error_info

    @classmethod
    def deserialize(cls, data: dict) -> LiveStream:
        playback_urls_data = data.get('playbackUrls')
        publish_endpoint_data = data.get('publishEndpoint')
        dvr_data = data.get('dvr')
        state_notification_data = data.get('stateNotification')
        enforced_stream_params_data = data.get('enforcedStreamParams')
        publisher_geo_data = data.get('publisherGeo')

        stream_type = data.get('streamType', StreamType.live)
        project_id = data['projectId']
        streamer_id = data['streamerId']
        stream_id = data['id']
        playback_urls = LiveStream._get_playback_urls(playback_urls_data)
        publish_endpoint = StreamPublishEndpoint.deserialize(publish_endpoint_data) if publish_endpoint_data else None
        dvr = StreamDVR.deserialize(dvr_data) if dvr_data else None
        state = data['state']
        duration = data['duration']
        max_publish_duration = data['maxPublishDuration']
        state_notification = StreamStateNotification.deserialize(state_notification_data) \
            if state_notification_data else None

        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        success = data.get('success')
        error_message = data.get('errorMessage')
        connect_timeout_secs = data.get('connectTimeout')
        reconnect_timeout_secs = data.get('reconnectTimeout')
        probe_result = data.get('probeResult')
        protocol = data['protocol']
        enforced_stream_params = EnforcedStreamParams.deserialize(enforced_stream_params_data) \
            if enforced_stream_params_data else None
        publisher_geo = GeoLocation.deserialize(publisher_geo_data) if publisher_geo_data else None
        error_code = data.get('errorCode')
        error_info = cls.deserialize_error_info(error_code, data.get('errorInfo'))

        return cls(project_id, streamer_id, stream_id, playback_urls, publish_endpoint, dvr, state,
                   duration, max_publish_duration, date_created, date_updated, state_notification, stream_type,
                   success, error_message, connect_timeout_secs, reconnect_timeout_secs, probe_result, protocol,
                   enforced_stream_params, publisher_geo, error_code, error_info)

    @classmethod
    def _get_playback_urls(cls, playback_urls_data):
        return [StreamPlayback.deserialize(playback) for playback in
                playback_urls_data] if playback_urls_data else None

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'projectId': self.project_id,
            'streamerId': self.streamer_id,
            'publishEndpoint': self.publish_endpoint.serialize() if self.publish_endpoint else None,
            'playbackUrls': [playback.serialize() for playback in self.playback],
            'dvr': self.dvr.serialize() if self.dvr else None,
            'duration': self.duration,
            'maxPublishDuration': self.max_publish_duration,
            'success': self.success,
            'errorMessage': self.error_message,
            'stateNotification': self.state_notification.serialize() if self.state_notification else None,
            'state': self.state,
            'connectTimeout': self.connect_timeout_secs,
            'reconnectTimeout': self.reconnect_timeout_secs,
            'probeResult': self.probe_result,
            'protocol': self.protocol,
            'enforcedStreamParams': self.enforced_stream_params.serialize() if self.enforced_stream_params else None,
            'publisherGeo': self.publisher_geo.serialize() if self.publisher_geo else None,
            'streamType': self.stream_type,
            'dateCreated': datetime_serialization.serialize(self.date_created),
            'dateUpdated': datetime_serialization.serialize(self.date_updated),
            'errorCode': self.error_code,
            'errorInfo': self.error_info.serialize() if self.error_info else None
        }

    @classmethod
    def deserialize_error_info(cls, error_code: StreamErrorCode, data: dict) -> StreamErrorInfo or None:
        if error_code == StreamErrorCode.stream_params_out_of_range:
            return StreamParamsOutOfRangeErrorInfo.deserialize(data)
        else:
            return None
