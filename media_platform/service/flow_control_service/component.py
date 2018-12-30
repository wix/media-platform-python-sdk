from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification
from media_platform.job.create_archive_job import CreateArchiveSpecification
from media_platform.job.extract_archive_job import ExtractArchiveSpecification
from media_platform.job.extract_poster_job import ExtractPosterSpecification
from media_platform.job.extract_storyboard_job import ExtractStoryboardSpecification
from media_platform.job.import_file_job import ImportFileSpecification
from media_platform.job.specification import Specification
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.lang.serialization import Deserializable, Serializable
from media_platform.service.flow_control_service.callback_specification import CallbackSpecification


class ComponentType(object):
    create_archive = 'archive.create'
    extract_archive = 'archive.extract'
    transcode = 'av.transcode'
    extract_poster = 'av.poster'
    extract_storyboard = 'av.storyboard'
    playlist = 'av.create_urlset'
    import_file = 'file.import'
    replace_extra_metadata = 'av.extra_metadata.replace'
    callback = 'flow.callback'


_SPECIFICATIONS = {
    ComponentType.create_archive: CreateArchiveSpecification,
    ComponentType.extract_archive: ExtractArchiveSpecification,
    ComponentType.transcode: TranscodeSpecification,
    ComponentType.extract_poster: ExtractPosterSpecification,
    ComponentType.extract_storyboard: ExtractStoryboardSpecification,
    ComponentType.playlist: None,
    ComponentType.import_file: ImportFileSpecification,
    ComponentType.replace_extra_metadata: ReplaceAudioExtraMetadataSpecification,
    ComponentType.callback: CallbackSpecification
}


class Component(Serializable, Deserializable):
    def __init__(self, component_type, successors=None, specification=None, delete_sources=False):
        # type: (ComponentType, [str], Specification, bool) -> None
        super(Component, self).__init__()

        self.type = component_type
        self.successors = successors or []
        self.specification = specification
        self.delete_sources = delete_sources

    def serialize(self):
        # type: () -> dict
        return {
            'type': self.type,
            'successors': self.successors,
            'specification': self.specification.serialize() if self.specification else None,
            'deleteSources': self.delete_sources
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Component
        component_type = data['type']
        specification_type = _SPECIFICATIONS[component_type]

        specification = None
        if specification_type:
            specification = specification_type.deserialize(data['specification'])

        return Component(component_type,
                         specification,
                         data.get('successors', []),
                         data.get('deleteSources', False))
