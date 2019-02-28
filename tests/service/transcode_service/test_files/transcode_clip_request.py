transcode_clip_request = {
    'specifications': [{
        'video': None,
        'destination': {
            'directory': '/',
            'path': None,
            'lifecycle': None,
            'acl': 'public',
            'bucket': None
        },
        'quality': 'aac_128',
        'qualityRange': None,
        'audio': None,
        'clipping': {
            'start': 3,
            'duration': 6,
            'fadeInDuration': 1,
            'fadeOutDuration': 2,
            'fadeInOffset': 4,
            'fadeOutOffset': 5
        }
    }],
    'sources': [{
        'path': '/audio.mp3',
        'fileId': None
    }],
    'jobCallback': None
}
