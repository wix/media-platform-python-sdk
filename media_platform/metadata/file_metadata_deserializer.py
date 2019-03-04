from media_platform.lang.serialization import Deserializable
from media_platform.metadata.audio_file_metadata import AudioFileMetadata
from media_platform.metadata.file_metadata import FileMetadata, MediaType
from media_platform.metadata.font_file_metadata import FontFileMetadata
from media_platform.metadata.image_file_metadata import ImageFileMetadata
from media_platform.metadata.video_file_metadata import VideoFileMetadata


class _FileMetadataDeserializer(Deserializable):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FileMetadata
        media_type = data['mediaType']

        if media_type == MediaType.video:
            return VideoFileMetadata.deserialize(data)
        elif media_type == MediaType.image:
            return ImageFileMetadata.deserialize(data)
        elif media_type == MediaType.audio:
            return AudioFileMetadata.deserialize(data)
        elif media_type == MediaType.font:
            return FontFileMetadata.deserialize(data)
        else:
            return FileMetadata.deserialize(data)
