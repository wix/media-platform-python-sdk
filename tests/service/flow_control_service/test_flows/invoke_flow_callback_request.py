invoke_flow_callback_request = {
    'invocation': {
        'sources': [],
        'entryPoints': ['import1']
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
                    'acl': 'public'
                }
            },
            'successors': ['callback1'],
            'type': 'file.import'
        },
        'callback1': {
            'deleteSources': False,
            'specification': {
                'url': 'http://requestbin.fullcontact.com/sc9kxnsc',
                'attachment': {'attachment-key': 'attachment-value'},
                'headers': {'header': 'value'},
                'passthrough': False,
            },
            'successors': [],
            'type': 'flow.callback'
        }
    }
}
