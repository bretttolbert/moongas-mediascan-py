from dataclasses import dataclass
from dataclass_wizard.v0 import YAMLWizard

from .artistdata import ArtistData


@dataclass
class Artist(YAMLWizard):
    """
    Artist dataclass
    an artist, including directory path and the data read from the artist.yml file in said directory
    """

    artist_data: ArtistData
    path: str
