class AudioQuality(object):
    mp3_128 = 'mp3_128'
    mp3_256 = 'mp3_256'
    mp3_320 = 'mp3_320'
    aac_128 = 'aac_128'
    aac_196 = 'aac_196'
    aac_256 = 'aac_256'
    aac_320 = 'aac_320'
    flac = 'flac'
    alac = 'alac'

    values = [
        mp3_128,
        mp3_256,
        mp3_320,
        aac_128,
        aac_256,
        aac_320,
        flac,
        alac,
    ]

    @classmethod
    def has_value(cls, value):
        # type: (str) -> bool
        return value in cls.values
