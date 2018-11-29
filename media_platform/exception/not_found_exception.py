from media_platform.exception.media_platform_exception import MediaPlatformException


class NotFoundException(MediaPlatformException):
    def __init__(self, cause=None, *args, **kwargs):
        super(NotFoundException, self).__init__(cause, *args, **kwargs)
