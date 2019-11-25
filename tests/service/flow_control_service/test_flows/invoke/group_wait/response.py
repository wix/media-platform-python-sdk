invoke_flow_group_wait_response = {
    'invocation': {
        'sources': [
            {
                'path': '/source/path.txt',
                'fileId': None
            }
        ],
        'entryPoints': ['copy1', 'copy2'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'operations': {
        'copy1': {
            'status': 'success',
            'deleteSources': False,
            'jobs': [],
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path1.txt',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                }
            },
            'results': [
                {
                    'mimeType': 'text/plain',
                    'hash': None,
                    'urn': 'urn:file:123',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/destination/path1.txt',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'public',
                    'type': '-',
                    'id': 'abcd',
                    'size': 123,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [
                {
                    'path': '/source/path.txt',
                    'fileId': None
                }
            ],
            'successors': ['group-wait'],
            'callback': None,
            'type': 'file.copy'
        },
        'copy2': {
            'status': 'success',
            'deleteSources': False,
            'jobs': [],
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path2.txt',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                }
            },
            'results': [
                {
                    'mimeType': 'text/plain',
                    'hash': None,
                    'urn': 'urn:file:123',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/destination/path2.txt',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'public',
                    'type': '-',
                    'id': 'abcd',
                    'size': 123,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [
                {
                    'path': '/source/path.txt',
                    'fileId': None
                }
            ],
            'successors': ['group-wait'],
            'callback': None,
            'type': 'file.copy'
        },
        'group-wait': {
            'status': 'waiting',
            'deleteSources': False,
            'jobs': [],
            'specification': None,
            'results': [
                {
                    'mimeType': 'text/plain',
                    'hash': None,
                    'urn': 'urn:file:123',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/destination/path1.txt',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'public',
                    'type': '-',
                    'id': 'abcd',
                    'size': 123,
                    'lifecycle': None
                },
                {
                    'mimeType': 'text/plain',
                    'hash': None,
                    'urn': 'urn:file:123',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/destination/path2.txt',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'public',
                    'type': '-',
                    'id': 'abcd',
                    'size': 123,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [
                {
                    'path': '/destination/path1.txt',
                    'fileId': None
                },
                {
                    'path': '/destination/path2.txt',
                    'fileId': None
                }
            ],
            'successors': ['group-wait'],
            'callback': None,
            'type': 'flow.group_wait'
        }
    },
    'id': '12342134',
    'status': 'success',
    'error': None,
}
