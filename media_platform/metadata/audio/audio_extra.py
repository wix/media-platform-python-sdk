from media_platform.lang.serialization import Deserializable
from media_platform.metadata.audio.attached_image import AttachedImage
from media_platform.metadata.audio.lyrics import Lyrics


class AudioExtra(Deserializable):
    def __init__(self, track_name=None, artist=None, album_name=None, track_number=None, genre=None, composer=None,
                 year=None, images=None, lyrics=None):
        # type: (str, str, str, str, str, str, str, [AttachedImage], Lyrics) -> None

        self.track_name = track_name
        self.artist = artist
        self.album_name = album_name
        self.track_number = str(track_number) if track_number is not None else None
        self.genre = genre
        self.composer = composer
        self.year = year

        self.images = images or []
        self.lyrics = lyrics

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioExtra

        lyrics_data = data.get('lyrics')

        images_data = data.get('images')
        if images_data:
            images = [AttachedImage.deserialize(image_data) for image_data in images_data if image_data]
        else:
            images = []

        lyrics = Lyrics.deserialize(lyrics_data) if lyrics_data else None

        return cls(data.get('trackName'), data.get('artist'), data.get('albumName'), data.get('trackNumber'),
                   data.get('genre'), data.get('composer'), data.get('year'), images, lyrics)
