from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


# http://id3.org/id3v2.4.0-frames (clause 4.14)
class AttachedImage(Serializable, Deserializable):
    def __init__(self, picture_type: str, mime_type: str = None, url: str = None):
        self.picture_type = picture_type
        self.mime_type = mime_type  # "image/png" or "image/jpeg"
        self.url = url  # mime tag will be  "-->" if url

    @classmethod
    def deserialize(cls, data: dict) -> AttachedImage:
        return AttachedImage(data.get('type'), data.get('mimeType'), data.get('url'))

    def serialize(self) -> dict:
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
