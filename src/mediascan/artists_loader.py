from .artists import Artists


def load_artists_yaml(yaml_fname: str) -> Artists:
    """
    raises: yaml.YAMLError
    """
    files = None
    with open(yaml_fname, "r") as stream:
        files = Artists.from_yaml(stream)  # type: ignore
    return files  # type: ignore
