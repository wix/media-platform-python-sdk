from media_platform.exception.media_platform_exception import MediaPlatformException


class ForbiddenException(MediaPlatformException):
    def __init__(self, cause=None, *args, **kwargs):
        super(ForbiddenException, self).__init__(cause, *args, **kwargs)
