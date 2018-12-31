from media_platform.lang.serialization import Serializable, Deserializable


class Clipping(Serializable, Deserializable):
    def __init__(self, start=None, duration=None, fade_in_duration=None, fade_out_duration=None, fade_in_offset=None,
                 fade_out_offset=None):
        # type: (int, int, int, int, int, int) -> None
        self.start = start
        self.duration = duration
        self.fade_in_duration = fade_in_duration
        self.fade_out_duration = fade_out_duration
        self.fade_in_offset = fade_in_offset
        self.fade_out_offset = fade_out_offset

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Clipping
        return cls(data.get('start'), data.get('duration'), data.get('fadeInDuration'), data.get('fadeOutDuration'),
                   data.get('fadeInOffset'), data.get('fadeOutOffset'))

    def serialize(self):
        # type: () -> dict
        return {
            'start': self.start,
            'duration': self.duration,
            'fadeInDuration': self.fade_in_duration,
            'fadeOutDuration': self.fade_out_duration,
            'fadeInOffset': self.fade_in_offset,
            'fadeOutOffset': self.fade_out_offset
        }

    # todo: Add validate()
