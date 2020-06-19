# -*- coding: UTF-8 -*-
"""Gets updated version of exercises.

Checks for existing version and won't overwrite.
"""
import os
import requests

LOCAL = os.path.dirname(os.path.realpath(__file__))


def get_the_updates() -> None:
    """Decide if the other functions should download each file."""
    base = ("https://raw.githubusercontent.com/"
            "notionparallax/code1161base/master")
    new_files = [
        "/week2/exercise0.py",
        "/week4/IOexamples.py",
        "/week5/exercise1.py",
        "/week5/exercise2.py"
        ""
    ]

    for f in new_files:
        save_path = "./" + f
        if not os.path.isfile(save_path) and f is not "":
            url = base + f
            print(("downloading", url))
            download_and_save(url, save_path)
        elif f is "":
            pass  # do nothing, it's padding
        else:
            print(f"You already have {f}")


def get_file_text(url: str) -> str:
    """Pull the raw file and return it as a string."""
    r = requests.get(url)
    return r.text.encode('utf-8')


def download_and_save(url: str, save_path: str) -> None:
    """Save a string as a file."""
    f = open(os.path.join(LOCAL, save_path), 'w')
    f.write(get_file_text(url))
    f.close()


get_the_updates()
