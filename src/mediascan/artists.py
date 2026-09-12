from dataclasses import dataclass
from dataclass_wizard.v0 import YAMLWizard

from .artist import Artist


@dataclass
class Artists(YAMLWizard):
    """
    Artists dataclass
    Data model for artists.yml file (multiple artist.yml are scanned into one consolidated artists.yml) output by mediascan cmd/scanartists

    """

    artists: list[Artist]
