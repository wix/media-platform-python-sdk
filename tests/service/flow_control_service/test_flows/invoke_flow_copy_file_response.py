invoke_flow_copy_file_response = {
    'invocation': {
        'sources': [
            {
                'path': '/source/path.txt',
                'fileId': None
            }
        ],
        'entryPoints': ['copyfile1'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'operations': {
        'copyfile1': {
            'status': 'success',
            'deleteSources': False,
            'jobs': [],
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path.txt',
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
                    'path': '/destination/path.txt',
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
            'successors': [],
            'callback': None,
            'type': 'file.copy'
        }
    },
    'id': '12342134',
    'status': 'success',
    'error': None,

}
