class MediaPlatformException(Exception):
    def __init__(self, message: str = None, cause: Exception = None):
        if cause:
            message = '%s: %s: %s' % (message, str(type(cause).__name__), str(cause))

        super(MediaPlatformException, self).__init__(message)
        self.cause = cause
