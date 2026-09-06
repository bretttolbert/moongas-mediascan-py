from dataclasses import dataclass
from dataclass_wizard.v0 import YAMLWizard
from dataclass_wizard.v0.enums import LetterCase

from .artistdata import ArtistData, ArtistDataOldFmt


@dataclass
class ArtistDataFile(YAMLWizard, key_transform=LetterCase.CAMEL):
    """
    ArtistDataFile dataclass
    Data model for a single artist_data.yaml YAML file

    """

    artist_data: ArtistData


@dataclass
class ArtistDataFileOldFmt(YAMLWizard, key_transform=LetterCase.CAMEL):
    """
    ArtistDataFile dataclass
    Data model for a single artist_data.yaml YAML file

    """

    artist_data: ArtistDataOldFmt
