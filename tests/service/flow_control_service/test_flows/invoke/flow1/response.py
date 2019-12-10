invoke_flow1_response = {
    'invocation': {
        'sources': [],
        'entryPoints': ['import'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'operations': {
        'import': {
            'status': 'success',
            'deleteSources': False,
            'jobs': ['g_1'],
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/imports/video.mp4',
                    'acl': 'public',
                    'lifecycle': None,
                    'bucket': None
                },
                'externalAuthorization': None,
                'sourceUrl': 'https://fish.com/dag.gadol'
            },
            'callback': None,
            'results': [
                {
                    'mimeType': 'video/mp4',
                    'hash': None,
                    'urn': 'urn:file:123',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/imports/video.mp4',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'public',
                    'type': '-',
                    'id': 'abcd',
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
            'jobs': ['g2_1', 'g2_2', 'g2_3', 'g2_4', 'g2_5'],
            'deleteSources': False,
            'specification': {
                'quality': None,
                'destination': {
                    'directory': '/deliverables/',
                    'path': None,
                    'acl': 'public',
                    'lifecycle': None,
                    'bucket': None
                },
                'video': None,
                'qualityRange': {
                    'minimum': '720p',
                    'maximum': '1080p'
                },
                'audio': None,
                'clipping': None
            },
            'callback': None,
            'results': [
                {
                    'mimeType': 'video/mp4',
                    'hash': '56566',
                    'dateCreated': '2018-01-10T16:11:36Z',
                    'path': '/deliverables/720p/video.mp4',
                    'dateUpdated': '2018-01-10T16:11:36Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '2341234',
                    'size': 2607390,
                    'lifecycle': None
                },
                {
                    'mimeType': 'video/mp4',
                    'hash': '6773f38357a87b4a37681aa17620ae6c',
                    'dateCreated': '2018-01-10T16:11:42Z',
                    'path': '/deliverables/1080p/video.mp4',
                    'dateUpdated': '2018-01-10T16:11:42Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '3243241',
                    'size': 5517966,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [
                {
                    'path': '/imports/video.mp4',
                    'fileId': '2345234534'
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
            'callback': None,
            'results': [
                {
                    'mimeType': 'video/mp4',
                    'hash': '56566',
                    'dateCreated': '2018-01-10T16:11:36Z',
                    'path': '/deliverables/720p/video.mp4',
                    'dateUpdated': '2018-01-10T16:11:36Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '12341324',
                    'size': 2607390,
                    'lifecycle': None
                },
                {
                    'mimeType': 'video/mp4',
                    'hash': '6773f38357a87b4a37681aa17620ae6c',
                    'dateCreated': '2018-01-10T16:11:42Z',
                    'path': '/deliverables/1080p/video.mp4',
                    'dateUpdated': '2018-01-10T16:11:42Z',
                    'acl': 'public',
                    'type': '-',
                    'id': '21341324',
                    'size': 5517966,
                    'lifecycle': None
                }
            ],
            'extraResults': {
                'urlset': '//fishenzon.com/deliverables/,720p,1080p,/video.mp4.urlset/master.m3u8'
            },
            'sources': [
                {
                    'path': '/deliverables/720p/video.mp4',
                    'fileId': '2341234'
                },
                {
                    'path': '/deliverables/1080p/video.mp4',
                    'fileId': '1234234'
                }
            ],
            'successors': [],
            'type': 'av.create_urlset'
        }
    },

    'id': '12342134',
    'status': 'success',
    'error': None
}
