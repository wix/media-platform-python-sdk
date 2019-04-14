from media_platform.lang.serialization import Serializable


class AttachedImage(Serializable):
    # http://id3.org/id3v2.4.0-frames (clause 4.14)

    def __init__(self, picture_type, mime_type=None, url=None):
        # type: (str, str, str) -> None
        super(AttachedImage, self).__init__()
        self.picture_type = picture_type
        self.mime_type = mime_type  # "image/png" or "image/jpeg"
        self.url = url  # mime tag will be  "-->" if url

    @classmethod
    def deserialize(cls, data):
        return AttachedImage(data.get('type'), data.get('mimeType'), data.get('url'))

    def serialize(self):
        return {
            'type': self.picture_type,
            'mimeType': self.mime_type,
            'url': self.url
        }


#    Picture type:  $00  Other
#                   $01  32x32 pixels 'file icon' (PNG only)
#                   $02  Other file icon
#                   $03  Cover (front)
#                   $04  Cover (back)
#                   $05  Leaflet page
#                   $06  Media (e.g. label side of CD)
#                   $07  Lead artist/lead performer/soloist
#                   $08  Artist/performer
#                   $09  Conductor
#                   $0A  Band/Orchestra
#                   $0B  Composer
#                   $0C  Lyricist/text writer
#                   $0D  Recording Location
#                   $0E  During recording
#                   $0F  During performance
#                   $10  Movie/video screen capture
#                   $11  A bright coloured fish
#                   $12  Illustration
#                   $13  Band/artist logotype
#                   $14  Publisher/Studio logotype
