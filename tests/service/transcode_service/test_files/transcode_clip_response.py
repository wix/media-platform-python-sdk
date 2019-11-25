transcode_clip_response = {
    'jobs': [
        {
            'issuer': 'urn:app:app-id',
            'type': 'urn:job:av.transcode',
            'id': 'g_1',
            'groupId': 'g',
            'status': 'pending',
            'sources': [
                {
                    'path': '/audio.mp3',
                    'fileId': 'source-id'
                }
            ],
            'specification': {
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
            },
            'result': None,
            'dateUpdated': '2017-06-25T12:13:32Z',
            'dateCreated': '2017-06-25T12:13:32Z',
        }
    ],
    'groupId': 'g'
}
