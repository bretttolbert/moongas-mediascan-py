from pathlib import Path
from typing import cast

from .artistdatafile import ArtistDataFile, ArtistDataFileOldFmt


def load_artistdatafile_yaml(yaml_fname: str) -> ArtistDataFile:
    """
    raises: FileNotFoundError, yaml.YAMLError
    """
    ret = None
    path = Path(yaml_fname)
    if not path.exists():
        raise FileNotFoundError(
            f"Moongas artist yaml file '{yaml_fname}' not found in current directory: {Path.cwd()}"
        )

    with open(path, "r") as stream:
        ret = cast(ArtistDataFile, getattr(ArtistDataFile, "from_yaml")(stream))
    return ret



def load_artistdatafile_yaml_old_fmt(yaml_fname: str) -> ArtistDataFileOldFmt:
    """
    raises: yaml.YAMLError
    """
    """
    raises: FileNotFoundError, yaml.YAMLError
    """
    ret = None
    path = Path(yaml_fname)
    if not path.exists():
        raise FileNotFoundError(
            f"Config file '{yaml_fname}' not found in current directory: {Path.cwd()}"
        )

    with open(path, "r") as stream:
        ret = cast(ArtistDataFileOldFmt, getattr(ArtistDataFileOldFmt, "from_yaml")(stream))
    return ret
