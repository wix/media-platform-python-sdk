class MediaPlatformException(Exception):
    def __init__(self, message=None, cause=None):
        # type: (str, Exception) -> None
        if (not message) and cause:
            message = str(cause)

        super(MediaPlatformException, self).__init__(message)
        self.cause = cause
