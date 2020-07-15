# -*- coding: UTF-8 -*-
"""Gets updated version of exercises.

Checks for existing version and won't overwrite.
"""
import os
import requests

LOCAL = os.path.dirname(os.path.realpath(__file__))


def get_the_updates() -> None:
    """Decide if the other functions should download each file."""
    base = "https://raw.githubusercontent.com/Design-Computing/me/master"
    new_files = [
        "/week5/exercise1.py",
    ]

    force_d = [
        "/week8/exercise1.py",
    ]
    for f in force_d:
        p = "./" + f
        if os.path.isfile(p):
            os.remove(p)

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
            print(
                "If you really want to update that file, "
                "delete it locally and rerun this script."
            )


def get_file_text(url: str) -> str:
    """Pull the raw file and return it as a string."""
    r = requests.get(url)
    return r.text


def download_and_save(url: str, save_path: str) -> None:
    """Save a string as a file."""
    f = open(os.path.join(LOCAL, save_path), "w")
    f.write(get_file_text(url))
    f.close()


get_the_updates()
