from media_platform.exception.media_platform_exception import MediaPlatformException


class UnauthorizedException(MediaPlatformException):
    def __init__(self, cause=None, *args, **kwargs):
        super(UnauthorizedException, self).__init__(cause, *args, **kwargs)
