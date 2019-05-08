invoke_flow_convert_font_response = {
    'invocation': {
        'sources': [
            {
                'fileId': None,
                'path': '/source/font.ttf'
            }
        ],
        'entryPoints': ['addSources1'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'operations': {
        'convert-font': {
            'status': 'waiting',
            'deleteSources': False,
            'jobs': ['g_1'],
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/font.woff',
                    'bucket': None,
                    'lifecycle': None,
                    'acl': 'private'
                },
                'fontSet': None,
                'fontType': 'woff'
            },
            'callback': None,
            'results': [
                {
                    'mimeType': 'application/x-font-woff',
                    'hash': None,
                    'urn': 'urn:file:123',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/destination/font.woff',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'private',
                    'type': '-',
                    'id': 'abcd',
                    'size': 1234,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [
                {
                    'fileId': None,
                    'path': '/source/font.ttf'
                }
            ],
            'successors': [],
            'type': 'font.convert'
        }
    },
    'id': '12342134',
    'status': 'working',
    'error': None
}
