wix_transparent_transcode_response = {
    'jobs': [
        {
            'issuer': 'urn:app:app-id',
            'type': 'urn:job:av.transcode',
            'id': 'g_1',
            'groupId': 'g',
            'status': 'pending',
            'sources': [
                {
                    'path': '/video.mp4',
                    'fileId': 'source-id'
                }
            ],
            'specification': {
                'quality': '480p',
                'destination': {
                    'directory': None,
                    'path': '/video.480p.mp4',
                    'acl': 'public',
                    'bucket': None
                },
                'video': {
                    'type': 'video',
                    'specification': {
                        'filters': [{
                            'name': 'makeWixTransparent',
                        }],
                        'frameRate': '25.0',
                        'frameRateFraction': '30000/1001',
                        'codec': {
                            'profile': 'main',
                            'maxRate': 6000000,
                            'crf': 20,
                            'name': 'h.264',
                            'level': '3.1'
                        },
                        'resolution': {
                            'width': 768,
                            'height': 480
                        },
                        'keyFrame': 50
                    }
                },
                'audio': {
                    'type': 'audio',
                    'specification': {
                        'channels': 'stereo',
                        'codec': {
                            'cbr': 3112,
                            'name': 'aac'
                        }
                    }
                },
                'clipping': None
            },
            'result': None,
            'dateUpdated': '2017-06-25T12:13:32Z',
            'dateCreated': '2017-06-25T12:13:32Z',
        }
    ],
    'groupId': 'g'
}
