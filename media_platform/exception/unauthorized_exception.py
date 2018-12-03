from typing import Any

from media_platform.exception.media_platform_exception import MediaPlatformException


class UnauthorizedException(MediaPlatformException):
    def __init__(self, cause=None, *args):
        # type: (Exception, Any) -> None
        super(UnauthorizedException, self).__init__(cause, *args)
