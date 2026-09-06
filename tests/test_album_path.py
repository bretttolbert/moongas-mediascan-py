
from mediascan.utils.path.album_path import AlbumPathBuilder


def test_albumpathbuilder_good_path():
    a = AlbumPathBuilder.of("/home/brett/Downloads/data/Music/Lil Wayne/Tha Carter IV [2011]")
    assert str(a.path) == "/home/brett/Downloads/data/Music/Lil Wayne/Tha Carter IV [2011]"
    assert a.valid == True
    assert a.artist_dirname == "Lil Wayne"
    assert a.album_dirname == "Tha Carter IV [2011]"
    assert a.year == 2011


def test_albumpathbuilder_bad_path_trailing_space():
    a = AlbumPathBuilder.of("/home/brett/Downloads/data/Music/Lil Wayne/Tha Carter IV [2011] ")
    assert str(a.path) == "/home/brett/Downloads/data/Music/Lil Wayne/Tha Carter IV [2011] "
    assert a.valid == False
    assert a.artist_dirname == "Lil Wayne"
    assert a.album_dirname == "Tha Carter IV [2011] "
    assert a.year == 2011
