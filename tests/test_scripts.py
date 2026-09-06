import pytest

from scripts.copy_covers import (
    copy_covers,
    copy_all,
    CopyCoversDestinationOptions,
)
from scripts.convert_covers import convert_all

"""
Just a place for hooks for running or debugging the scripts 
"""


def test_copy_covers():
    copy_covers(
        "/data/Music/",
        "/data/Covers/",
        "cover.jpg",
        CopyCoversDestinationOptions.PreserveStructure,
        exclude_keywords=["Sepulga"],
        dry_run=True,
        overwrite=False,
    )


@pytest.mark.skip()
def test_copy_all():
    copy_all()


@pytest.mark.skip()
def test_convert_all():
    convert_all()
