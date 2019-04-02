invoke_flow_operation_callback_response = {
    'invocation': {
        'sources': [],
        'entryPoints': ['import1'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'operations': {
        'import1': {
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
                'sourceUrl': 'https://fish.com/dag.gadol'
            },

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
            'successors': [],
            'callback': {
                'url': 'http://requestbin.fullcontact.com/sc9kxnsc',
                'attachment': {'attachment-key': 'attachment-value'},
                'headers': {'header': 'value'},
                'passthrough': False,
            },
            'type': 'file.import'
        },
    },
    'id': '12342134',
    'status': 'success',
    'error': None,

}
