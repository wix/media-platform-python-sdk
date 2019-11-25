invoke_flow_convert_font_request = {
    'invocation': {
        'sources': [
            {
                'fileId': None,
                'path': '/source/font.ttf'
            }
        ],
        'entryPoints': ['convert-font'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'flow': {
        'convert-font': {
            'deleteSources': False,
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
            'successors': [],
            'type': 'font.convert',
            'sources': [],
        }
    }
}
