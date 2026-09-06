from dataclasses import dataclass
from dataclass_wizard.v0 import YAMLWizard

from .artist import Artist


@dataclass
class Artists(YAMLWizard):
    """
    Artists dataclass
    Data model for artists.yaml file output by mediascan cmd/scanartists

    """

    artists: list[Artist]
