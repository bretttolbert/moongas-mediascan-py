from dataclasses import dataclass


@dataclass
class MediaFile:
    """
    MediaFile dataclass

    """

    path: str
    size: int
    format: str
    title: str
    artist: str
    albumartist: str
    album: str
    genre: str
    year: int
    duration: int


@dataclass
class MediaFileWithArtistData(MediaFile):
    """
    Represents a mediafile with (scalar) artist data.
    This data is formed by joining the mediascan db
    mediafiles table with the artists data table.
    """

    artist_name: str
    city: str
    country_code: str
    region_code: str
    language_code: str
