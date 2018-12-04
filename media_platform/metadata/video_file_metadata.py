from media_platform.metadata.file_metadata import FileMetadata, MediaType
from media_platform.metadata.video.video_basic import VideoBasic
from media_platform.service.file_descriptor import FileDescriptor


class VideoFileMetadata(FileMetadata):
    def __init__(self, file_descriptor, basic=None):
        super(VideoFileMetadata, self).__init__(MediaType.video, file_descriptor, basic)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> VideoFileMetadata
        if data['mediaType'] != MediaType.video:
            raise ValueError('not video metadata')

        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])
        basic = VideoBasic.deserialize(data.get('basic')) if data.get('basic') else None

        return VideoFileMetadata(file_descriptor, basic)
