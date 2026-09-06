from dataclasses import dataclass
from dataclass_wizard.v0 import YAMLWizard

from .mediafile import MediaFile


@dataclass
class MediaFiles(YAMLWizard):
    """
    MediaFiles dataclass
    Data model for files.yaml file output by mediascan cmd/scanfiles

    """

    files: list[MediaFile]
