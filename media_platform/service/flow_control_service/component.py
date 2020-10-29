from __future__ import annotations

from media_platform.job.convert_font_job import ConvertFontSpecification
from media_platform.job.create_archive_job import CreateArchiveSpecification
from media_platform.job.extract_archive.extract_archive_job import ExtractArchiveSpecification
from media_platform.job.extract_poster_job import ExtractPosterSpecification
from media_platform.job.extract_storyboard_job import ExtractStoryboardSpecification
from media_platform.job.import_file_job import ImportFileSpecification
from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification
from media_platform.job.specification import Specification
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.lang.serialization import Deserializable, Serializable
from media_platform.service.callback import Callback
from media_platform.service.flow_control_service.specifications.add_sources_specification import AddSourcesSpecification
from media_platform.service.flow_control_service.specifications.copy_file_specification import CopyFileSpecification
from media_platform.service.source import Source


class ComponentType:
    create_archive = 'archive.create'
    extract_archive = 'archive.extract'
    transcode = 'av.transcode'
    extract_poster = 'av.poster'
    extract_storyboard = 'av.storyboard'
    playlist = 'av.create_urlset'
    import_file = 'file.import'
    copy_file = 'file.copy'
    replace_extra_metadata = 'av.extra_metadata.replace'
    convert_font = 'font.convert'
    add_sources = 'flow.add_sources'
    group_wait = 'flow.group_wait'


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
    ComponentType.convert_font: ConvertFontSpecification,
    ComponentType.add_sources: AddSourcesSpecification,
    ComponentType.group_wait: None,
}


class Component(Serializable, Deserializable):
    def __init__(self, component_type: ComponentType, successors: [str] = None, specification: Specification = None,
                 delete_sources: bool = False, callback: Callback = None, sources: [Source] = None):
        self.type = component_type
        self.successors = successors or []
        self.specification = specification
        self.delete_sources = delete_sources
        self.callback = callback
        self.sources = sources or []

    def serialize(self) -> dict:
        return {
            'type': self.type,
            'successors': self.successors,
            'specification': self.specification.serialize() if self.specification else None,
            'deleteSources': self.delete_sources,
            'callback': self.callback.serialize() if self.callback else None,
            'sources': [s.serialize() for s in self.sources]
        }

    @classmethod
    def deserialize(cls, data: dict) -> Component:
        specification_type = _SPECIFICATIONS[data['type']]
        specification = specification_type.deserialize(data['specification']) if specification_type else None

        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        sources = [Source.deserialize(s) for s in data.get('sources', [])]

        return cls(data['type'],
                   data.get('successors', []),
                   specification,
                   data.get('deleteSources', False),
                   callback,
                   sources)
