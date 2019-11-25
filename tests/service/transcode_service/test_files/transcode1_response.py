transcode1_response = {
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
                        'filter': 'scale=768:480,setsar=1/1',
                        'frameRate': '25.0',
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
        },
        {
            'issuer': 'urn:app:app-id',
            'type': 'urn:job:av.transcode',
            'id': 'g_2',
            'groupId': 'g',
            'status': 'pending',
            'sources': [
                {
                    'path': '/video.mp4',
                    'fileId': 'source-id'
                }
            ],
            'specification': {
                'quality': '720p',
                'destination': {
                    'directory': None,
                    'path': '/video.720p.mp4',
                    'acl': 'public'
                },
                'video': {
                    'type': 'video',
                    'specification': {
                        'filter': 'scale=1152:720,setsar=1/1',
                        'frameRate': '25.0',
                        'codec': {
                            'profile': 'high',
                            'maxRate': 6000000,
                            'crf': 20,
                            'name': 'h.264',
                            'level': '4.1'
                        },
                        'resolution': {
                            'width': 1152,
                            'height': 720
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
                }
            },
            'result': None,
            'dateUpdated': '2017-06-25T12:13:33Z',
            'dateCreated': '2017-06-25T12:13:33Z',
        },
    ],
    'groupId': 'g'
}
