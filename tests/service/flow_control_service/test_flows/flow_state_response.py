flow_state_response = {
    'invocation': {
        'sources': [],
        'entryPoints': [
            'import'
        ],
        'notification': None
    },
    'operations': {
        'import': {
            'status': 'success',
            'deleteSources': False,
            'jobs': [
                'g_1'
            ],
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/imports/video.mp4',
                    'acl': 'public',
                    'lifecycle': None
                },
                'sourceUrl': 'https://fish.com/dag.gadol'
            },
            'results': [
                {
                    'mimeType': 'video/mp4',
                    'hash': None,
                    'urn': 'urn:file:1354324',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/imports/video.mp4',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '1354324',
                    'size': 4151438,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [],
            'successors': [
                'transcode'
            ],
            'type': 'file.import'
        },
        'transcode': {
            'status': 'success',
            'jobs': [
                'g2_1',
                'g2_2',
            ],
            'deleteSources': False,
            'specification': {
                'quality': None,
                'destination': {
                    'directory': '/',
                    'path': None,
                    'acl': 'public',
                    'lifecycle': None
                },
                'video': None,
                'qualityRange': {
                    'minimum': '480p',
                    'maximum': '1440p'
                },
                'audio': None,
                'clipping': None
            },
            'results': [
                {
                    'mimeType': 'video/mp4',
                    'hash': '123123213',
                    'dateCreated': '2018-01-10T16:11:30Z',
                    'path': '/video.480p.mp4',
                    'dateUpdated': '2018-01-10T16:11:30Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '65454643',
                    'size': 1277825,
                    'lifecycle': None
                },
                {
                    'mimeType': 'video/mp4',
                    'hash': '56566',
                    'dateCreated': '2018-01-10T16:11:36Z',
                    'path': '/video.720p.mp4',
                    'dateUpdated': '2018-01-10T16:11:36Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '45345',
                    'size': 2607390,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [
                {
                    'path': '/imports/video.mp4',
                    'fileId': '1354324'
                }
            ],
            'successors': [
                'playlist'
            ],
            'type': 'av.transcode'
        },
        'playlist': {
            'status': 'success',
            'deleteSources': False,
            'jobs': [],
            'specification': None,
            'results': [
                {
                    'mimeType': 'video/mp4',
                    'hash': '123123213',
                    'urn': 'urn:file:65454643',
                    'dateCreated': '2018-01-10T16:11:30Z',
                    'path': '/video.480p.mp4',
                    'dateUpdated': '2018-01-10T16:11:30Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '65454643',
                    'size': 1277825,
                    'lifecycle': None
                },
                {
                    'mimeType': 'video/mp4',
                    'hash': '56566',
                    'dateCreated': '2018-01-10T16:11:36Z',
                    'path': '/video.720p.mp4',
                    'dateUpdated': '2018-01-10T16:11:36Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '45345',
                    'size': 2607390,
                    'lifecycle': None
                }
            ],
            'extraResults': {
                'urlset': '//fishenzon.com/video.,480p,720p,.mp4.urlset/master.m3u8'
            },
            'sources': [
                {
                    'path': '/video.480p.mp4',
                    'fileId': '65454643'
                },
                {
                    'path': '/video.720p.mp4',
                    'fileId': '45345'
                }
            ],
            'successors': [],
            'type': 'av.create_urlset'
        }
    },
    'id': '49eca277747047c5833f15a0eed137b9',
    'status': 'success',
    'error': None
}
