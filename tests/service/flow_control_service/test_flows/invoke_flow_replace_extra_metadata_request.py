invoke_flow_replace_extra_metadata_request = {
    'invocation': {
        'sources': [],
        'entryPoints': ['metadata1']
    },
    'flow': {
        'metadata1': {
            'deleteSources': False,
            'specification': {
                'source': {
                    'path': '/source/path.mp3',
                    'fileId': None
                },
                'destination': {
                    'directory': None,
                    'path': '/destination/path.mp3',
                    'lifecycle': None,
                    'acl': 'private'
                },
                'audioExtraMetadata': {
                    'trackName': 'track_name',
                    'lyrics': {
                        'lang': 'eng',
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
            'successors': [],
            'type': 'av.extra_metadata.replace'
        }
    }
}