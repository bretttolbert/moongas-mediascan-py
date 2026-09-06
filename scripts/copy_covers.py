from enum import Enum
import os
from pathlib import Path
import shutil
import subprocess


class CopyCoversDestinationOptions(Enum):
    SingleDirectory = 1  #  All images copies to single destination directory, replacing filenames with 00001.jpg etc.
    PreserveStructure = 2  #  Preserve directory structure and filenames in destination


def copy_covers(
    source_path: str,
    dest_path: str,
    cover_filename: str = "cover.jpg",
    dest_opts: CopyCoversDestinationOptions = CopyCoversDestinationOptions.PreserveStructure,
    exclude_keywords: list[str] = [],
    dry_run: bool = False,
    overwrite: bool = False,
    skip_if_converted_exists_in_dest: bool = True,
) -> int:
    """
    Recursively copy album cover images from source directory
    to specified destination directory.

    Copy Covers Destination Options:
    1. SingleDirectory
    All images copies to single destination directory, replacing filenames with 00001.jpg etc.
    2. PreserveStructure
    Preserve directory structure and filenames in destination

    Returns number it copied (or would have copied if not dry_run)
    """
    if overwrite and os.path.exists(dest_path):
        subprocess.run(["rm", "-rf", dest_path], check=True)
    Path(dest_path).mkdir(parents=True, exist_ok=True)
    count = 0

    # first make the directories
    if dest_opts == CopyCoversDestinationOptions.PreserveStructure:
        for root, dirs, files in os.walk(source_path, topdown=False):
            for sd in dirs:
                source_dir_abs_path = Path(root).joinpath(sd)
                source_dir_rel_path = source_dir_abs_path.relative_to(source_path)
                dest_abs_path = Path(dest_path).joinpath(source_dir_rel_path)
                if not dry_run:
                    dest_abs_path.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(source_path, topdown=False):
        for fname in files:
            for keyword in exclude_keywords:
                if root.find(keyword) != -1:
                    continue
            if fname == cover_filename:
                source_file_abs_path = Path(root).joinpath(fname)
                source_file_rel_path = source_file_abs_path.relative_to(source_path)
                dest_abs_path = Path(dest_path)
                if dest_opts == CopyCoversDestinationOptions.SingleDirectory:
                    ext = Path(cover_filename).suffix
                    fname = str(count + 1).rjust(5, "0") + ext
                    dest_abs_path = dest_abs_path.joinpath(fname)
                elif dest_opts == CopyCoversDestinationOptions.PreserveStructure:
                    dest_abs_path = dest_abs_path.joinpath(source_file_rel_path)
                if overwrite or not dest_abs_path.exists():
                    fbase, _ = os.path.splitext(dest_abs_path)
                    # if .webp already exists in destination, skip copying .jpg
                    dest_abs_path_converted = Path(fbase + ".webp")
                    if (
                        not skip_if_converted_exists_in_dest
                        or not dest_abs_path_converted.exists()
                    ):
                        if not dry_run:
                            shutil.copy(source_file_abs_path, dest_abs_path)
                        count += 1
    return count


def copy_covers_dir(
    name: str,
    cover_filename: str="cover.jpg",
    exclude_keywords: list[str] = [],
    dry_run: bool=False,
    overwrite: bool=False,
    skip_if_converted_exists_in_dest: bool=True,
) -> int:
    count = copy_covers(
        f"/data/{name}/",
        f"/data/Covers/{name}/",
        cover_filename,
        CopyCoversDestinationOptions.PreserveStructure,
        exclude_keywords=exclude_keywords,
        dry_run=dry_run,
        overwrite=overwrite,
        skip_if_converted_exists_in_dest=skip_if_converted_exists_in_dest,
    )
    print(f"Total copied for dir {name}: {count}")
    return count


def copy_all():
    covers_path = Path("/data/Covers")
    covers_path.mkdir(parents=True, exist_ok=True)
    exclude_keywords = ["Sepulga"]
    dry_run = False
    overwrite = False
    skip_if_converted_exists_in_dest = True
    count = 0
    for d in ("Music", "MusicOther"):
        count += copy_covers_dir(
            d,
            exclude_keywords=exclude_keywords,
            dry_run=dry_run,
            overwrite=overwrite,
            skip_if_converted_exists_in_dest=skip_if_converted_exists_in_dest,
        )
    print(f"Total copied for all dirs: {count}")


def main():
    copy_all()


if __name__ == "__main__":
    main()
