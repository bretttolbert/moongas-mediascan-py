import sys

from mediascan.mediafiles import MediaFiles
from mediascan.mediafiles_loader import load_files_yaml


def list_artists(files: MediaFiles):
    artists: set[str] = set()
    for f in files.files:
        artists.add(f.artist)
    for a in artists:
        print(a)


def main():
    if len(sys.argv) != 2:
        print("Usage: {0} <files yaml file>".format(sys.argv[0]))
    else:
        files = load_files_yaml(sys.argv[1])
        list_artists(files)


if __name__ == "__main__":
    main()
