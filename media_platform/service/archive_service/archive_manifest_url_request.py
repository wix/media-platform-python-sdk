

class ArchiveManifestUrlRequest(object):
    def __init__(self, domain):
        # type: (str) -> None

        self._url = '//archive-' + domain.replace('.appspot.com', '.wixmp.com')

        self.path = None

    def set_path(self, path):
        # type: (str) -> ArchiveManifestUrlRequest
        self.path = path
        return self

    def execute(self):
        # type: () -> str

        return self._url + self.path
