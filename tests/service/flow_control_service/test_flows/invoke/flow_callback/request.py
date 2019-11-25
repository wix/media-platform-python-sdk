invoke_flow_callback_request = {
    'invocation': {
        'sources': [],
        'entryPoints': ['import1'],
        'callback': {
            'url': 'http://requestbin.fullcontact.com/sc9kxnsc',
            'attachment': {'attachment-key': 'attachment-value'},
            'headers': {'header': 'value'},
            'passthrough': False,
        },
        'errorStrategy': 'stopOnError'
    },
    'flow': {
        'import1': {
            'deleteSources': False,
            'specification': {
                'sourceUrl': 'http://movs.me/video.mp4',
                'destination': {
                    'directory': None,
                    'path': '/imports/video.mp4',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                }
            },
            'successors': [],
            'callback': None,
            'type': 'file.import',
            'sources': [],
        },
    }
}
