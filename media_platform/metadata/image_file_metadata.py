from media_platform.metadata.file_metadata import FileMetadata, MediaType
from media_platform.metadata.image.image_basic import ImageBasic
from media_platform.metadata.image.image_features import ImageFeatures
from media_platform.service.file_descriptor import FileDescriptor


class ImageFileMetadata(FileMetadata):
    def __init__(self, file_descriptor, basic=None, features=None):
        # type: (FileDescriptor, ImageBasic, ImageFeatures) -> None
        super(ImageFileMetadata, self).__init__(MediaType.image, file_descriptor, basic)

        self.features = features

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImageFileMetadata
        if data['mediaType'] != MediaType.image:
            raise ValueError('not image metadata')

        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])
        basic = ImageBasic.deserialize(data.get('basic')) if data.get('basic') else None
        features = ImageFeatures.deserialize(data.get('features')) if data.get('features') else None

        return ImageFileMetadata(file_descriptor, basic, features)
