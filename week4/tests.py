# -*- coding: UTF-8 -*-
"""Week 4 tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

from colorama import Fore
from colorama import Style
from datetime import datetime
from func_timeout import func_timeout, FunctionTimedOut
from pathlib import Path
import importlib.util as importUtils
import json
import math
import mock
import os
import random
import requests
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import (
    completion_message,
    ex_runs,
    finish_up,
    lab_book_entry_completed,
    loadExerciseFile,
    nyan_cat,
    syntax_error_message,
    test,
)

EM = Fore.YELLOW
NORM = Fore.WHITE

WEEK_NUMBER = 4
LOCAL = os.path.dirname(os.path.realpath(__file__))
TIMEOUT_IN_SECONDS = 10

# if working dir contains week, we are one too deep
if "week" in os.getcwd():
    os.chdir("..")


def find_lasers(path):
    """Look for a file that contains only the number 6."""
    path = path + "/week4/lasers.pew"
    if os.path.isfile(path):
        return int(open(path).read()) == int(6)
    else:
        print(
            "can't find lasers.pew, did you make it?"
            " Does it have exactly that file name?"
            "looking in " + path
        )
        return False


# def tzOffset():
#     """Return tz in hours for current locale."""
#     ts = time.time()
#     utc_offset = (
#         datetime.fromtimestamp(ts) - datetime.utcfromtimestamp(ts)
#     ).total_seconds()
#     seconds_in_hour = 60 * 60
#     return utc_offset / seconds_in_hour


# def treat():
#     """Go and get the coloured ascii face particular to this person."""
#     with open(".git/config", "r") as f:
#         for line in f:
#             if ("url = https://github.com/" in line) and not ("notionparallax" in line):
#                 # ensure it's not Ben's repo
#                 print(line)
#                 name = line.split("/")[-2]
#                 if "git" in name:
#                     # if ssh url
#                     name = name.split(":")[-1]
#             elif "url = https://github.com/notionparallax" in line:
#                 print("we must be testing the tests")
#                 name = "notionparallax"
#     try:
#         url = (
#             "https://raw.githubusercontent.com/"
#             "notionparallax/code1161base/master/faces/"
#         )
#         full_url = url + name
#         print("treat:\n", full_url, requests.get(full_url).text)
#     except Exception as e:
#         print("Error with getting github username", e)


def theTests(path_to_code_to_check="."):
    """Run the tests."""
    print("\nWelcome to week {}!".format(WEEK_NUMBER))
    print("May the odds be ever in your favour.\n")

    path = "{}/week{}/exercise1.py".format(path_to_code_to_check, WEEK_NUMBER)
    print(path)

    exercise1 = loadExerciseFile(
        path_to_code_to_check, weekNumber=WEEK_NUMBER, exerciseNumber=1
    )

    testResults = []

    # stack the tests below here
    testDict = {"lastName": "hoogmoed", "password": "jokers", "postcodePlusID": 4311240}
    testResults.append(
        test(
            exercise1.get_some_details() == testDict,
            "Exercise 1: get some data out of a JSON file",
        )
    )

    lengths = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
    testName = "Exercise 1: request some words from the internet"
    try:
        pyramid = exercise1.wordy_pyramid()
        p_lengths = [len(w) for w in pyramid]
        if pyramid is not None:
            testResults.append(test(p_lengths == lengths, testName))
            if p_lengths != lengths:
                print(
                    pyramid,
                    "Read the next line as (your word length, test word length)",
                    list(zip(p_lengths, lengths)),
                    p_lengths == lengths,
                    sep="\n",
                )
        else:
            testResults.append(test(False, testName))
            print(
                "The tests didn't get anything back from your code, "
                "are you doing a return?"
            )
    except Exception as e:
        testResults.append(test(False, testName))
        print(testName, e)

    ex_name = "Exercise 1: Consult the Pokedex."
    poke_tries = [
        {
            "args": (70, 80),
            "result": {"name": "victreebel", "weight": 155, "height": 17},
            "gift": pokeball(),
        },
        {
            "args": (9, 15),
            "result": {"name": "blastoise", "weight": 855, "height": 16},
            "gift": tiny_pikachu(),
        },
        {
            "args": (55, 57),
            "result": {"name": "golduck", "weight": 766, "height": 17},
            "gift": squirtle(),
        },
        {
            "args": (0, 3),
            "result": {"name": "ivysaur", "weight": 130, "height": 10},
            "gift": pikachu(),
        },
    ]
    for p in poke_tries:
        try:
            r = func_timeout(
                TIMEOUT_IN_SECONDS, exercise1.pokedex, args=list(p["args"])
            )
            if r == p["result"]:
                print(p["gift"])
            else:
                print("expecting", p["result"], "got", r)
            testResults.append(test(r == p["result"], ex_name))
        except FunctionTimedOut as ftoe:
            print(
                ex_name,
                ftoe,
                "check your numbers/ algorithm efficiency,",
                "or maybe just your internet speed.",
                "This shouldn't be taking so long",
            )
        except Exception as e:
            testResults.append(0)
            print(ex_name, e)

    testResults.append(
        test(find_lasers(path_to_code_to_check), "Exercise 1: count the lasers.")
    )

    message = "Rad, you've got all the tests passing!"

    return finish_up(testResults, message, nyan_cat())


def pokeball():
    return """
────────▄███████████▄────────
─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────
────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────
───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───
──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──
─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─
██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██
███████████░░███░░███████████
██░░░░░░░██░░███░░██░░░░░░░██
██░░░░░░░░██░░░░░██░░░░░░░░██
██░░░░░░░░░███████░░░░░░░░░██
─██░░░░░░░░░░░░░░░░░░░░░░░██─
──██░░░░░░░░░░░░░░░░░░░░░██──
───██░░░░░░░░░░░░░░░░░░░██───
────███░░░░░░░░░░░░░░░███────
─────▀███░░░░░░░░░░░███▀─────
────────▀███████████▀────────"""


def tiny_pikachu():
    return r"""
/\︿╱\
\0_ 0 /╱\╱ 
\▁︹_/
    """


def pikachu():
    return """
░█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀ """


def squirtle():
    return r"""
;-.               ,
 \ '.           .'/
  \  \ .---. .-' /
   '. '     `\_.'
     |(),()  |     ,
     (  __   /   .' \
    .''.___.'--,/\_,|
   {  /     \   }   |
    '.\     /_.'    /
     |'-.-',  `; _.'
     |  |  |   |`
     `""`""`"'"`"""


if __name__ == "__main__":
    theTests()
