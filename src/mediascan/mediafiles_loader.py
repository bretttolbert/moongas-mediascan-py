from pathlib import Path
from typing import cast

from .mediafiles import MediaFiles


def load_files_yaml(yaml_fname: str) -> MediaFiles:
    """
    raises: FileNotFoundError, yaml.YAMLError
    """
    ret = None
    path = Path(yaml_fname)
    if not path.exists():
        raise FileNotFoundError(
            f"Moongas mediafiles yaml file '{yaml_fname}' not found in current directory: {Path.cwd()}"
        )

    with open(path, "r") as stream:
        ret = cast(MediaFiles, getattr(MediaFiles, "from_yaml")(stream))
    return ret