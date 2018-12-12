import os

from media_platform.service.file_descriptor import FileDescriptor


class PlaylistRequest(object):
    # https://github.com/kaltura/nginx-vod-module#multi-url-structure
    URL_SET = '{url}{prefix},{renditions},{postfix}.urlset/master.m3u8'

    def __init__(self, domain):
        # type: (str) -> None

        self._url = '//packager-' + domain.replace('.appspot.com', '.wixmp.com')

        self.file_descriptors = []
        self.paths = []

    def set_files(self, file_descriptors):
        # type: ([FileDescriptor]) -> PlaylistRequest
        self.file_descriptors = file_descriptors
        return self

    def add_files(self, *file_descriptors):
        # type: ([FileDescriptor]) -> PlaylistRequest
        self.file_descriptors.extend(file_descriptors)
        return self

    def set_paths(self, paths):
        # type: ([str]) -> PlaylistRequest
        self.paths = paths
        return self

    def add_paths(self, *paths):
        # type: ([str]) -> PlaylistRequest
        self.paths.extend(paths)
        return self

    def execute(self):
        # type: () -> str
        paths = [file_descriptor.path for file_descriptor in self.file_descriptors]
        paths.extend(self.paths)

        common_prefix = self._common_prefix(paths)
        common_suffix = self._common_suffix(paths)

        renditions = [path.replace(common_prefix, '').replace(common_suffix, '') for path in paths]

        return self.URL_SET.format(url=self._url,
                                   prefix=common_prefix,
                                   renditions=','.join(renditions),
                                   postfix=common_suffix)

    @staticmethod
    def _common_prefix(paths):
        # type: ([str]) -> str
        return os.path.commonprefix(paths)

    @staticmethod
    def _common_suffix(paths):
        # type: ([str]) -> str
        reversed_paths = [path[::-1] for path in paths]

        reversed_common = os.path.commonprefix(reversed_paths)

        return reversed_common[::-1]
