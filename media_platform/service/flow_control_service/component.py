from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification
from media_platform.job.create_archive_job import CreateArchiveSpecification
from media_platform.job.extract_archive_job import ExtractArchiveSpecification
from media_platform.job.extract_poster_job import ExtractPosterSpecification
from media_platform.job.extract_storyboard_job import ExtractStoryboardSpecification
from media_platform.job.import_file_job import ImportFileSpecification
from media_platform.job.specification import Specification
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.lang.serialization import Deserializable, Serializable
from media_platform.service.callback import Callback
from media_platform.service.flow_control_service.specifications.add_sources_specification import AddSourcesSpecification
from media_platform.service.flow_control_service.specifications.copy_file_specification import CopyFileSpecification


class ComponentType(object):
    create_archive = 'archive.create'
    extract_archive = 'archive.extract'
    transcode = 'av.transcode'
    extract_poster = 'av.poster'
    extract_storyboard = 'av.storyboard'
    playlist = 'av.create_urlset'
    import_file = 'file.import'
    copy_file = 'file.copy'
    replace_extra_metadata = 'av.extra_metadata.replace'
    add_sources = 'flow.add_sources'


_SPECIFICATIONS = {
    ComponentType.create_archive: CreateArchiveSpecification,
    ComponentType.extract_archive: ExtractArchiveSpecification,
    ComponentType.transcode: TranscodeSpecification,
    ComponentType.extract_poster: ExtractPosterSpecification,
    ComponentType.extract_storyboard: ExtractStoryboardSpecification,
    ComponentType.playlist: None,
    ComponentType.import_file: ImportFileSpecification,
    ComponentType.copy_file: CopyFileSpecification,
    ComponentType.replace_extra_metadata: ReplaceAudioExtraMetadataSpecification,
    ComponentType.add_sources: AddSourcesSpecification
}


class Component(Serializable, Deserializable):
    def __init__(self, component_type, successors=None, specification=None, delete_sources=False, callback=None):
        # type: (ComponentType, [str], Specification, bool, Callback) -> None
        super(Component, self).__init__()

        self.type = component_type
        self.successors = successors or []
        self.specification = specification
        self.delete_sources = delete_sources
        self.callback = callback

    def serialize(self):
        # type: () -> dict
        return {
            'type': self.type,
            'successors': self.successors,
            'specification': self.specification.serialize() if self.specification else None,
            'deleteSources': self.delete_sources,
            'callback': self.callback.serialize() if self.callback else None
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Component
        specification_type = _SPECIFICATIONS[data['type']]
        specification = specification_type.deserialize(data['specification']) if specification_type else None

        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None

        return cls(data['type'],
                   specification,
                   data.get('successors', []),
                   data.get('deleteSources', False),
                   callback)
