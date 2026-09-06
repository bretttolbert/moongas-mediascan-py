import os
import subprocess
from pathlib import Path

"""
Script to batch convert covers from jpg to webp (in place),
optionally deleting the source jpgs.
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


def convert_covers(
    source_root: str,
    source_filename: str = "cover.jpg",
    dest_filename: str = "cover.webp",
    exclude_keywords: list[str] = [],
    resolution: str = "1000x1000",
    quality: int = 80,
    dry_run: bool = False,
    delete_source_file: bool = True,
    overwrite: bool = False,
) -> int:
    """
    Recursively batch convert images from one format to another,
    with the specified resolution and quality settings.
    The conversion is performed in place.

    Returns the number it converted (or would have converted if not dry_run)

    """

    count = 0
    for root, _, files in os.walk(source_root, topdown=False):
        for fname in files:
            for keyword in exclude_keywords:
                if root.find(keyword) != -1:
                    continue
            if fname == source_filename:
                if overwrite or not Path(root).joinpath(dest_filename).exists():
                    if not dry_run:
                        cmd = [
                            "convert",
                            source_filename,
                            "-resize",
                            resolution,
                            "-quality",
                            str(quality),
                            dest_filename,
                        ]
                        print(f"root={root} cmd={cmd}")
                        subprocess.run(cmd, cwd=root, check=True)
                        if delete_source_file:
                            os.remove(source_filename)
                    count += 1
    return count


def convert_covers_dir(covers_dir: str) -> int:
    count = convert_covers(
        f"{covers_dir}/",
        "cover.jpg",
        "cover.webp",
        exclude_keywords=[""],
        resolution="1000x1000",
        quality=80,
        dry_run=False,
        delete_source_file=True,
        overwrite=False,
    )
    print(f"Total converted for dir {covers_dir}: {count}")
    return count


def convert_all():
    count = 0
    count += convert_covers_dir("/data/Covers/Music")
    count += convert_covers_dir("/data/Covers/MusicOther")
    print(f"Total converted for all dirs: {count}")
    make_archive = False
    if make_archive:
        archive_path = Path(f"/data/Covers.tar.gz")
        if archive_path.exists():
            print("Removing existing archive")
            os.remove(archive_path)
        subprocess.run(
            ["tar", "czvf", str(archive_path), "/data/Covers/"],
            check=True,
        )


def main():
    convert_all()


if __name__ == "__main__":
    main()
