import os
import subprocess
from pathlib import Path


"""
Script to batch convert video from one format (e.g. wmv) to mp4 (x264) (in place),
optionally deleting the source video files.
"""


def convert_all(
    source_root: Path,
    source_ext: str = ".wmv",
    dest_ext: str = ".h264.mp4",
    exclude_keywords: list[str] = [],
    delete_source_file: bool = True,
    overwrite: bool = False,
    dry_run: bool = False,
) -> int:
    """
    Recursively batch convert images from one format to another,
    with the specified resolution and quality settings.
    The conversion is performed in place.

    Returns the number it converted (or would have converted if not dry_run)

    """

    starting_directory = os.getcwd()
    count = 0
    for root, _, files in os.walk(source_root, topdown=False):
        for fname in files:
            for keyword in exclude_keywords:
                if root.find(keyword) != -1:
                    continue
            if fname.endswith(source_ext):
                source_base, source_ext = os.path.splitext(fname)
                dest_filename = source_base + dest_ext
                dest_path = Path(root).joinpath(dest_filename)
                cmd = f"ffmpeg -i '{fname}' -c:v libx264 -c:a aac '{dest_filename}'"
                print(f"root={root} cmd={cmd}")
                os.chdir(root)
                if overwrite or not dest_path.exists():
                    if not dry_run:
                        subprocess.run(
                            [
                                "ffmpeg",
                                "-i",
                                fname,
                                "-c:v",
                                "libx264",
                                "-c:a",
                                "aac",
                                dest_filename,
                            ],
                            check=False,
                        )
                if delete_source_file:
                    os.remove(fname)
                os.chdir(starting_directory)
                count += 1
    return count


def main():
    # default config:
    OUTPUT_FMTS = ["h264.mp4"]
    SOURCE_ROOT = "/videos"
    SOURCE_EXT = ".wmv"
    OVERWRITE = False
    DELETE_SOURCE_FILES = True
    DRY_RUN = False

    for dest_fmt in OUTPUT_FMTS:
        # recommend a fixed-height resolution with a variable width
        # consider square flags like Switzerland
        # if we matched the width, it would look out of proportion
        source_path = Path(f"{SOURCE_ROOT}/")
        dest_ext = f".{dest_fmt}"
        # convert in place folder), then delete original
        count = convert_all(
            source_root=source_path.resolve(),
            source_ext=SOURCE_EXT,
            dest_ext=dest_ext,
            delete_source_file=DELETE_SOURCE_FILES,
            overwrite=OVERWRITE,
            dry_run=DRY_RUN,
        )
        print(f"converted {count} videos")


if __name__ == "__main__":

    main()
