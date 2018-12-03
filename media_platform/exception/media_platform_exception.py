from typing import Any


class MediaPlatformException(Exception):
    def __init__(self, cause=None, *args):
        # type: (Exception, Any) -> None
        super(MediaPlatformException, self).__init__(*args)
        
        self.cause = cause
