invoke_flow_copy_file_request = {
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
    'flow': {
        'copyfile1': {
            'deleteSources': False,
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path.txt',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                }
            },
            'successors': [],
            'callback': None,
            'type': 'file.copy',
            'sources': [],
        },
    }
}
