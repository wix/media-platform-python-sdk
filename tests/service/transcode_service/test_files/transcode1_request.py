transcode1_request = {
    'specifications': [{
        'video': None,
        'destination': {
            'directory': '/',
            'path': None,
            'lifecycle': None,
            'acl': 'public',
            'bucket': None
        },
        'quality': None,
        'qualityRange': {
            'minimum': '480p',
            'maximum': '1080p'
        },
        'audio': None,
        'clipping': None
    }],
    'sources': [{
        'path': '/video.mp4',
        'fileId': None
    }],
    'jobCallback': None
}
