class MediaPlatformException(Exception):
    def __init__(self, message=None, cause=None):
        # type: (str, Exception) -> None
        if cause:
            message = '%s: %s: %s' % (message, str(type(cause).__name__), str(cause))

        super(MediaPlatformException, self).__init__(message)
        self.cause = cause
