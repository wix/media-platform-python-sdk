invoke_flow_with_add_sources_request = {
    'invocation': {
        'sources': [],
        'entryPoints': ['addSources1', 'addSources2'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'flow': {
        'addSources1': {
            'deleteSources': False,
            'specification': {
                'sources': [{
                    'path': '/source/path.mp3',
                    'fileId': None
                }]
            },
            'callback': None,
            'successors': ['metadata1'],
            'type': 'flow.add_sources',
            'sources': [],
        },
        'addSources2': {
            'deleteSources': False,
            'specification': {
                'sources': [{
                    'path': '/source/path2.mp3',
                    'fileId': None
                }]
            },
            'callback': None,
            'successors': ['metadata2'],
            'type': 'flow.add_sources',
            'sources': [],
        },
        'metadata1': {
            'deleteSources': False,
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path.mp3',
                    'lifecycle': None,
                    'acl': 'private',
                    'bucket': None
                },
                'audioExtraMetadata': {
                    'trackName': 'track_name',
                    'lyrics': {
                        'lang': 'eng',
                        'language': 'eng',
                        'text': 'text',
                        'description': 'lyrics_description'
                    },
                    'artist': 'artist',
                    'image': {
                        'url': 'image_url',
                        'mimeType': 'mime_type',
                        'description': 'image_description'
                    },
                    'albumName': 'album_name',
                    'composer': 'composer',
                    'year': 'year',
                    'genre': 'genre',
                    'trackNumber': 'track_number'
                }
            },
            'callback': None,
            'successors': [],
            'type': 'av.extra_metadata.replace',
            'sources': [],
        },
        'metadata2': {
            'deleteSources': False,
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/destination/path2.mp3',
                    'lifecycle': None,
                    'acl': 'private',
                    'bucket': None
                },
                'audioExtraMetadata': {
                    'trackName': 'track_name',
                    'lyrics': {
                        'lang': 'eng',
                        'language': 'eng',
                        'text': 'text',
                        'description': 'lyrics_description'
                    },
                    'artist': 'artist',
                    'image': {
                        'url': 'image_url',
                        'mimeType': 'mime_type',
                        'description': 'image_description'
                    },
                    'albumName': 'album_name',
                    'composer': 'composer',
                    'year': 'year',
                    'genre': 'genre',
                    'trackNumber': 'track_number'
                }
            },
            'callback': None,
            'successors': [],
            'type': 'av.extra_metadata.replace',
            'sources': [],
        }
    }
}
