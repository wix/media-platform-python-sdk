import os

from demo.globals import demo_path, client
from media_platform.service.live_service.live_stream import LiveStream
from media_platform.service.live_service.stream_protocol import StreamProtocol

archive_path = demo_path + '/archive1.zip'
extracted_path = demo_path + '/extracted'
report_path = extracted_path + '/report.csv'


def live_stream_demo():
    stream = client.live_service.open_stream_request().\
        set_connect_timeout(60).\
        set_reconnect_timeout(60).\
        set_protocol(StreamProtocol.rtmp).\
        execute() # type: LiveStream

    server, stream_key = os.path.split(stream.publish_endpoint.url)
    print('Server: ' + server)
    print('Stream Key: ' + stream_key)
    print('Playback url: https:' + stream.playback[0].path)

    stream = client.live_service.get_stream_request().set_id(stream.id).execute()
    print('Got stream: %s' % stream.serialize())


if __name__ == '__main__':
    live_stream_demo()
