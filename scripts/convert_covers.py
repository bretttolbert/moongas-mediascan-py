import os
import subprocess
from pathlib import Path

"""
Script to batch convert covers from jpg to webp (in place),
optionally deleting the src jpgs.
By default it converts at 80% quality and 1000x1000 resolution.

To check the progress, in a separate terminal you can do this:

This number should be going up:

$ find /data/Covers -name "*.webp" | wc -l
533

This number should be going down:

$ find /data/Covers -name "*.jpg" | wc -l
4068

Before:

$ du -shc /data/Covers
1.3G	/data/Covers
1.3G	total

After:

$ du -shc /data/Covers
439M	/data/Covers
439M	total

Etc.

Typical workflow to update covers on my server:

$ python scripts/copy_covers.py
$ python scripts/convert_covers.py
$ rsync -ahvP /data/Covers/ root@$DROPLET_IP:/var/www/html/Covers/ --delete

"""


def convert_medialib_cover_images_inplace(
    src_path: Path,
    src_fname: str = "cover.jpg",
    dst_fname: str = "cover.webp",
    exclude_keywords: list[str] = [],
    resolution: str = "1000x1000",
    quality: int = 80,
    dry_run: bool = False,
    delete_src_file: bool = True,
    overwrite: bool = False,
) -> int:
    """
    Recursively batch convert images (in place) from one format to another,
    with the specified resolution and quality settings.

    Returns the number it converted (or would have converted if not dry_run)

    src_path: path to medialib e.g. '/data/Music'
    src_fname: the source filename to match e.g. 'cover.jpg'
    dst_fname: the destination filename to convert to e.g. 'cover.webp'
    delete_src_file: whether or not to delete source file after conversion (default=true)
    """
    count = 0
    for root, _, files in os.walk(src_path, topdown=False):
        for fname in files:
            for keyword in exclude_keywords:
                if root.find(keyword) != -1:
                    continue
            if fname == src_fname:
                if overwrite or not Path(root).joinpath(dst_fname).exists():
                    if not dry_run:
                        cmd = [
                            "convert",
                            src_fname,
                            "-resize",
                            resolution,
                            "-quality",
                            str(quality),
                            dst_fname,
                        ]
                        print(f"root={root} cmd={cmd}")
                        subprocess.run(cmd, cwd=root, check=True)
                        if delete_src_file:
                            os.remove(src_fname)
                    count += 1
    return count


def convert_medialibs_cover_images_inplace(src_paths: list[Path]) -> int:
    count: int = 0
    for src_path in src_paths:
        count = convert_medialib_cover_images_inplace(
            src_path,
            "cover.jpg",
            "cover.webp",
            exclude_keywords=[""],
            resolution="1000x1000",
            quality=80,
            dry_run=False,
            delete_src_file=True,
            overwrite=False,
        )
        print(f"Total converted for medialib dir {src_path}: {count}")
    print(f"Grand total copied for all medialib dirs: {count}")
    return count


def make_archive(src_path: Path, dst_path: Path):
    """
    src_path: path to the source directory to compress
    dst_path: path to the .tgz file to output
    """
    if dst_path.exists():
        print(f"Removing existing archive {dst_path}")
        os.remove(dst_path)
    subprocess.run(
        ["tar", "czvf", str(dst_path), str(src_path)],
        check=True,
    )


def main():
    convert_medialibs_cover_images_inplace([Path("/data/Covers/Music"), Path("/data/Covers/MusicOther")])
    make_archive(Path("/data/Covers/"), Path(f"/data/Covers.tar.gz"))


if __name__ == "__main__":
    main()
