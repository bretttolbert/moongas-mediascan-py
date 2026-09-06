import os
import shlex
import subprocess


def make_warning_video(source_filename: str = "warning.jpg", dest_filename: str="warning.mp4"):
    """Obligatory epilepsy warning
    warning.jpg from https://static1.squarespace.com/static/5759b194f85082811025c4cd/58460a4ed2b857e0d8abc4b9/5de8972b05b927237727e848/1582069779595/epilepsy+.jpg?format=1500w
    """
    if os.path.exists(dest_filename):
        os.remove(dest_filename)
    ffmpeg_cmd = (
        # "ffmpeg -framerate {}".format(10)
        # + " -t 5 -loop 1 -i "
        "ffmpeg"
        + " -framerate 1/0.015 -i "
        + source_filename
        + " -c:v libx264 -pix_fmt yuv420p -vf scale=1200:1200 "
        + dest_filename
    )
    print(ffmpeg_cmd)
    subprocess.run(shlex.split(ffmpeg_cmd), check=True)


def make_covers_video(
    source_root: str = "/data/Covers/",
    source_ext: str = ".jpg",
    dest_filename: str = "covers.mp4",
    frame_rate: int = 10,
):
    """
    Executes an ffmpeg command to output a video made from
    the album cover images in the specified directory.
    """
    if os.path.exists(dest_filename):
        os.remove(dest_filename)
    ffmpeg_cmd = (
        "ffmpeg -framerate {}".format(frame_rate)
        + f" -pattern_type glob -i '{source_root}*{source_ext}'"
        + " -c:v libx264 -pix_fmt yuv420p -vf scale=1200:1200 "
        + dest_filename
    )
    print(ffmpeg_cmd)
    subprocess.run(shlex.split(ffmpeg_cmd), check=True)


def concat_videos(
    filenames_to_concat: list[str] = ["warning.mp4", "covers.mp4"],
    dest_filename: str = "combined.mp4",
):
    """Concatenates warning video and covers video into combined output video"""
    if os.path.exists(dest_filename):
        os.remove(dest_filename)
    with open("list.txt", "w") as list_file:
        for fname in filenames_to_concat:
            list_file.write(f"file '{fname}'\n")
    ffmpeg_cmd = "ffmpeg -safe 0 -f concat -i list.txt -c copy " + dest_filename
    print(ffmpeg_cmd)
    subprocess.run(shlex.split(ffmpeg_cmd), check=True)


def main():
    # assumes you've ran copy_covers with SingleDirectory
    # make_warning_video()
    make_covers_video(source_root="/data/CoversFlatDir/")
    # concat_videos()


if __name__ == "__main__":
    main()
