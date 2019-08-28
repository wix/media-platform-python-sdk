wix_transparent_transcode_request = {
    'specifications': [{
        'clipping': None,
        'qualityRange': None,
        'destination': {
            'directory': None,
            'path': '/video.720.mp4',
            'bucket': None,
            'lifecycle': None,
            'acl': 'public'
        },
        'video': {
            'type': 'video',
            'skip': False,
            'specification': {
                'resolution': {
                    'width': 256,
                    'height': 144,
                    'sampleAspectRatio': '1:1',
                    'scaling': {
                        'algorithm': 'lanczos'
                    },
                },
                'codec': {
                    'profile': 'main',
                    'name': 'h264',
                    'level': '3.1',
                    'maxRate': 10000,
                    'crf': 25,
                    'gop': {
                        'bAdapt': 0,
                        'bFrames': 2,
                        'bPyramid': 0,
                        'sceneCut': 0,
                        'keyInterval': 30,
                        'refFrame': 3,
                        'minKeyInterval': 30
                    },
                    'preset': 'faster'
                },
                'filters': [{
                    'name': 'makeWixTransparent',
                    'settings': {}
                }],
                'frameRateFraction': '30000/1001'
            },
            'copy': False
        },
        'audio': None,
        'quality': None
    }],
    'sources': [{
        'path': '/video.mp4',
        'fileId': None
    }],
    'jobCallback': None
}
