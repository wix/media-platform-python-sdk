invoke_flow_operation_callback_request = {
    'invocation': {
        'sources': [],
        'entryPoints': ['import1'],
        'callback': None,
        'errorStrategy': 'stopOnError',
        'operationCallbackStatusFilter': ['error', 'success'],
    },
    'flow': {
        'import1': {
            'deleteSources': False,
            'specification': {
                'sourceUrl': 'http://movs.me/video.mp4',
                'externalAuthorization': None,
                'destination': {
                    'directory': None,
                    'path': '/imports/video.mp4',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                }
            },
            'successors': [],
            'callback': {
                'url': 'http://requestbin.fullcontact.com/sc9kxnsc',
                'attachment': {'attachment-key': 'attachment-value'},
                'headers': {'header': 'value'},
                'passthrough': False,
            },
            'type': 'file.import',
            'sources': [],
        },
    }
}
