invoke_flow_group_wait_request = {
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
    'flow': {
        'copy1': {
            'deleteSources': False,
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path1.txt',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                }
            },
            'successors': ['group-wait'],
            'callback': None,
            'type': 'file.copy',
            'sources': [],
        },
        'copy2': {
            'deleteSources': False,
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path2.txt',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                }
            },
            'successors': ['group-wait'],
            'callback': None,
            'type': 'file.copy',
            'sources': [],
        },
        'group-wait': {
            'deleteSources': False,
            'specification': None,
            'successors': [],
            'callback': None,
            'type': 'flow.group_wait',
            'sources': [],
        },
    }
}
