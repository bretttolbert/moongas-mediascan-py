from pathlib import Path

from scripts.copy_medialib import (
    copy_medialib,
    copy_medialibs,
    DirCopyMode,
)
from scripts.convert_covers import convert_medialibs_cover_images_inplace

def test_copy_covers(tmp_path: Path) -> None:
    src_path = tmp_path / "src"
    dst_path = tmp_path / "dst"
    copy_medialib(
        src_path,
        dst_path,
        include_filenames=["cover.jpg"],
        exclude_keywords=["Sepulga"],
        dry_run=True,
        ignore_existing=False,
        dir_copy_mode=DirCopyMode.PreserveStructure,
    )


def test_copy_all(tmp_path: Path):
    src_path1 = tmp_path / "src" / "lib1"
    src_path2 = tmp_path / "src" / "lib2"
    dst_path = tmp_path / "dst"
    copy_medialibs([src_path1, src_path2], dst_path)


def test_convert_all(tmp_path: Path):
    src_path1 = tmp_path / "src" / "lib1"
    src_path2 = tmp_path / "src" / "lib2"
    convert_medialibs_cover_images_inplace([src_path1, src_path2])
