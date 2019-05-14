invoke_flow_replace_extra_metadata_request = {
    'invocation': {
        'sources': [
            {
                'fileId': None,
                'path': '/source/path.mp3'
            }
        ],
        'entryPoints': ['metadata1'],
        'callback': None,
        'errorStrategy': 'stopOnError'
    },
    'flow': {
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
        }
    }
}
