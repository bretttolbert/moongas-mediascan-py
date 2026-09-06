from .artistdatafile import ArtistDataFile, ArtistDataFileOldFmt


def load_artistdatafile_yaml(yaml_fname: str) -> ArtistDataFile:
    """
    raises: yaml.YAMLError
    """
    files = None
    with open(yaml_fname, "r") as stream:
        files = ArtistDataFile.from_yaml(stream)  # type: ignore
    return files  # type: ignore


def load_artistdatafile_yaml_old_fmt(yaml_fname: str) -> ArtistDataFile:
    """
    raises: yaml.YAMLError
    """
    files = None
    with open(yaml_fname, "r") as stream:
        files = ArtistDataFileOldFmt.from_yaml(stream)  # type: ignore
    return files  # type: ignore
