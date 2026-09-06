import pytest

from pathlib import Path
from typing import Generator

from mediascan.utils.path.album_path import AlbumPathBuilder


@pytest.fixture(scope="function")
def good_album_path(tmp_path: Path) -> Generator[Path, None, None]:
    album_path = tmp_path / 'data' / 'Music' / 'Lil Wayne' / 'Tha Carter IV [2011]'
    album_path.mkdir(parents=True, exist_ok=True)
    assert album_path.exists() and album_path.is_dir()
    yield album_path


def test_albumpathbuilder_good_path(good_album_path: Path):
    assert good_album_path.exists() and good_album_path.is_dir()
    a = AlbumPathBuilder.of(str(good_album_path))
    assert str(a.path).endswith("/data/Music/Lil Wayne/Tha Carter IV [2011]")
    assert a.valid == True
    assert a.artist_dirname == "Lil Wayne"
    assert a.album_dirname == "Tha Carter IV [2011]"
    assert a.year == 2011


def test_albumpathbuilder_bad_path_trailing_space(good_album_path: Path):
    assert good_album_path.exists() and good_album_path.is_dir()
    a = AlbumPathBuilder.of(str(good_album_path) + " ")
    assert str(a.path).endswith("/data/Music/Lil Wayne/Tha Carter IV [2011] ")
    assert a.valid == False
    assert a.artist_dirname == "Lil Wayne"
    assert a.album_dirname == "Tha Carter IV [2011] "
    assert a.year == 2011
