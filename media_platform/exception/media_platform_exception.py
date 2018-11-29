from collections import Iterator


class MediaPlatformException(Exception):
    def __init__(self, cause=None, *args, **kwargs):
        # type: (Exception, Iterator, dict) -> None
        super(MediaPlatformException, self).__init__(*args, **kwargs)
        
        self.cause = cause
