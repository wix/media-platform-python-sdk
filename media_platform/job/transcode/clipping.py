from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class Clipping(Serializable, Deserializable):
    def __init__(self, start: int = None, duration: int = None, fade_in_duration: int = None,
                 fade_out_duration: int = None, fade_in_offset: int = None, fade_out_offset: int = None):
        self.start = start
        self.duration = duration
        self.fade_in_duration = fade_in_duration
        self.fade_out_duration = fade_out_duration
        self.fade_in_offset = fade_in_offset
        self.fade_out_offset = fade_out_offset

    @classmethod
    def deserialize(cls, data: dict) -> Clipping:
        return cls(data.get('start'), data.get('duration'), data.get('fadeInDuration'), data.get('fadeOutDuration'),
                   data.get('fadeInOffset'), data.get('fadeOutOffset'))

    def serialize(self) -> dict:
        return {
            'start': self.start,
            'duration': self.duration,
            'fadeInDuration': self.fade_in_duration,
            'fadeOutDuration': self.fade_out_duration,
            'fadeInOffset': self.fade_in_offset,
            'fadeOutOffset': self.fade_out_offset
        }

    # todo: Add validate()
