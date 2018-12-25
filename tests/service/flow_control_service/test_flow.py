from unittest import TestCase

from media_platform.job.import_file_job import ImportFileSpecification
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.service.destination import Destination
from media_platform.service.flow_control_service.component import Component, ComponentType
from media_platform.service.flow_control_service.flow import Flow


class TestFlow(TestCase):

    def test_valid(self):
        flow = Flow().add_component(
            'import',
            Component(ComponentType.import_file, ['transcode'],
                      ImportFileSpecification('http://movs.me/video.mp4', Destination('/imports/video.mp4')))
        ).add_component(
            'transcode',
            Component(ComponentType.transcode, ['playlist'],
                      TranscodeSpecification(Destination(directory='/deliverables/'),
                                             quality_range=VideoQualityRange(VideoQuality.res_720p,
                                                                             VideoQuality.res_1080p)))
        ).add_component(
            'playlist',
            Component(ComponentType.playlist, [])
        )

        flow.validate()

    def test_cyclic(self):
        flow = Flow().add_component(
            'a',
            Component(ComponentType.import_file, ['b'],
                      ImportFileSpecification('http://movs.me/video.mp4', Destination('/imports/video.mp4')))
        ).add_component(
            'b',
            Component(ComponentType.transcode, ['a'],
                      TranscodeSpecification(Destination(directory='/deliverables/'),
                                             quality_range=VideoQualityRange(VideoQuality.res_720p,
                                                                             VideoQuality.res_1080p)))
        )

        with self.assertRaises(ValueError):
            flow.validate()
