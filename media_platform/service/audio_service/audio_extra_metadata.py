from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.metadata.audio.lyrics import Lyrics


class Image(Serializable, Deserializable):
    def __init__(self, url: str, mime_type: str = None, description: str = None):
        self.url = url
        self.mime_type = mime_type
        self.description = description

    def serialize(self) -> dict:
        return {
            'url': self.url,
            'mimeType': self.mime_type,
            'description': self.description
        }

    @classmethod
    def deserialize(cls, data: dict) -> Image:
        return cls(data['url'], data.get('mimeType'), data.get('description'))


class AudioExtraMetadata(Serializable, Deserializable):
    def __init__(self, track_name: str = None, artist: str = None, album_name: str = None, track_number: str = None,
                 genre: str = None, composer: str = None, year: str = None, image: Image = None, lyrics: Lyrics = None):
        self.track_name = track_name
        self.artist = artist
        self.album_name = album_name
        self.track_number = track_number
        self.genre = genre
        self.composer = composer
        self.year = year
        self.image = image
        self.lyrics = lyrics

    def serialize(self) -> dict:
        data = {
            'trackName': self.track_name,
            'artist': self.artist,
            'albumName': self.album_name,
            'trackNumber': self.track_number,
            'genre': self.genre,
            'composer': self.composer,
            'year': self.year,
            'image': self.image.serialize() if self.image else None,
            'lyrics': self.lyrics.serialize() if self.lyrics else None,
        }

        return self._omit_empty(data)

    @classmethod
    def deserialize(cls, data: dict) -> AudioExtraMetadata:
        image_data = data.get('image')
        lyrics_data = data.get('lyrics')
        image = Image.deserialize(image_data) if image_data else None
        lyrics = Lyrics.deserialize(lyrics_data) if lyrics_data else None
        return cls(data.get('trackName'), data.get('artist'), data.get('albumName'), data.get('trackNumber'),
                   data.get('genre'), data.get('composer'), data.get('year'), image, lyrics)

    @staticmethod
    def _omit_empty(data: dict) -> dict:
        return {k: v for k, v in data.items() if v}
