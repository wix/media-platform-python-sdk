from media_platform.metadata.file_metadata import FileMetadata, MediaType
from media_platform.metadata.font.font_basic import FontBasic
from media_platform.service.file_descriptor import FileDescriptor


class FontFileMetadata(FileMetadata):
    def __init__(self, file_descriptor, basic=None):
        # type: (FileDescriptor, FontBasic) -> None
        super(FontFileMetadata, self).__init__(MediaType.font, file_descriptor, basic)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FontFileMetadata
        if data['mediaType'] != MediaType.font:
            raise ValueError('not font metadata')

        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])
        basic = FontBasic.deserialize(data.get('basic')) if data.get('basic') else None

        return FontFileMetadata(file_descriptor, basic)
