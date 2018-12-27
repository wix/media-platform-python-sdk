from media_platform.lang.serialization import Serializable, Deserializable


class Clipping(Serializable, Deserializable):
    def __init__(self, clip_start=None, clip_end=None, fade_in_duration=None, fade_out_duration=None,
                 fade_in_offset=None, fade_out_offset=None):
        # type: (int, int, int, int, int, int) -> None
        self.clip_start = clip_start
        self.clip_end = clip_end
        self.fade_in_duration = fade_in_duration
        self.fade_out_duration = fade_out_duration
        self.fade_in_offset = fade_in_offset
        self.fade_out_offset = fade_out_offset

    def serialize(self):
        return {
            'clipStart': self.clip_start,
            'clipEnd': self.clip_end,
            'fadeInDuration': self.fade_in_duration,
            'fadeOutDuration': self.fade_out_duration,
            'fadeInOffset': self.fade_in_offset,
            'fadeOutOffset': self.fade_out_offset
        }

    @classmethod
    def deserialize(cls, data):
        return cls(data.get('clipStart'), data.get('clipEnd'), data.get('fadeInDuration'), data.get('fadeOutDuration'),
                   data.get('fadeInOffset'), data.get('fadeOutOffset'))