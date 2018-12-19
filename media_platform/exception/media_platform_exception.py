class MediaPlatformException(Exception):
    def __init__(self, cause=None):
        # type: (Exception) -> None
        super(MediaPlatformException, self).__init__(str(cause) if cause else None)
        
        self.cause = cause
