from typing import Any

from media_platform.exception.media_platform_exception import MediaPlatformException


class ConflictException(MediaPlatformException):
    def __init__(self, cause=None, *args):
        # type: (Exception, Any) -> None
        super(ConflictException, self).__init__(cause, *args)
