invoke_flow1_request = {
    'invocation': {
        'sources': [],
        'entryPoints': ['import'],
        'callback': None
    },
    'flow': {
        'import': {
            'deleteSources': False,
            'specification': {
                'sourceUrl': 'http://movs.me/video.mp4',
                'destination': {
                    'directory': None,
                    'path': '/imports/video.mp4',
                    'lifecycle': None,
                    'acl': 'public'
                }
            },
            'callback': None,
            'successors': ['transcode'],
            'type': 'file.import'
        },
        'playlist': {
            'deleteSources': False,
            'specification': None,
            'callback': None,
            'successors': [],
            'type': 'av.create_urlset'
        },
        'transcode': {
            'deleteSources': False,
            'specification': {
                'video': None,
                'destination': {
                    'directory': '/deliverables/',
                    'path': None,
                    'lifecycle': None,
                    'acl': 'public'
                },
                'quality': None,
                'qualityRange': {
                    'minimum': '720p',
                    'maximum': '1080p'
                },
                'audio': None,
                'clipping': None
            },
            'callback': None,
            'successors': ['playlist'],
            'type': 'av.transcode'
        }
    }}

