from globals import demo_path, resources_dir, client
from media_platform import FileDescriptor, Source, Destination
from media_platform.job.job_group import JobGroup
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.job.transcode_job import TranscodeSpecification
from wait_for_results import wait_for_result_files

video_path = demo_path + '/video.mp4'
transcoded_path = demo_path + '/transcoded'

transcode_specification = TranscodeSpecification(
    Destination(transcoded_path),
    quality_range=VideoQualityRange(VideoQuality.res_360p, VideoQuality.res_720p)
)


def transcode_video_demo():
    video_file = upload_video()
    transcode_job_group = transcode_video(video_file)

    transcoded_files = wait_for_result_files(transcode_job_group)

    print_playlist_url(transcoded_files)


def upload_video():
    # type: () -> FileDescriptor
    print('Uploading video to %s...' % video_path)
    with open(resources_dir + '/video.mp4', 'rb') as archive:
        return client.file_service.upload_file_v2_request(). \
            set_path(video_path). \
            set_content(archive). \
            execute()


def transcode_video(video_file):
    # type: (FileDescriptor) -> JobGroup
    return client.transcode_service.transcode_request(). \
        add_sources(Source(video_file.path)). \
        add_specifications(transcode_specification). \
        execute()


def print_playlist_url(transcoded_files):
    playlist = client.transcode_service.playlist_request(). \
        add_files(*transcoded_files). \
        execute()
    print('Playlist url: https:%s' % playlist)
    print('')

if __name__ == '__main__':
    transcode_video_demo()
