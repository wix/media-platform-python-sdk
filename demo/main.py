from demo.extract_archive import extract_archive_demo
from demo.image_manipulation import image_manipulation_demo
from demo.transcode_video import transcode_video_demo
from demo.live_stream import live_stream_demo


def main():
    image_manipulation_demo()
    transcode_video_demo()
    extract_archive_demo()
    live_stream_demo()


if __name__ == '__main__':
    main()
