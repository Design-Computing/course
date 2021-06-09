# -*- coding: UTF-8 -*-
"""Week 4 tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

import importlib.util as importUtils
import json
import math
import os
import random
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import mock
import requests
from colorama import Fore, Style
from func_timeout import FunctionTimedOut, func_timeout

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
    timeout_message,
)

EM = Fore.YELLOW
NORM = Fore.WHITE

SET_NUMBER = 4
LOCAL = os.path.dirname(os.path.realpath(__file__))
TIMEOUT_IN_SECONDS = 10

# if working dir contains set, we are one too deep
if "set" in os.getcwd():
    os.chdir("..")


def find_lasers(path) -> bool:
    """Look for a file that contains only the number 6."""
    path = path + "/set4/lasers.pew"
    if os.path.isfile(path):
        count_in_file = int(open(path).read())
        return count_in_file == 6
    else:
        print(
            "can't find lasers.pew, did you make it?"
            " Does it have exactly that file name?"
            "looking in " + path
        )
        return False


def theTests(path_to_code_to_check: str = "../me") -> dict:
    """Run the tests."""
    print(f"\nWelcome to set {SET_NUMBER}!")
    print("May the odds be ever in your favour.\n")

    path = f"{path_to_code_to_check}/set{SET_NUMBER}/exercise1.py"
    print(path)

    exercise1 = loadExerciseFile(
        path_to_code_to_check, setNumber=SET_NUMBER, exerciseNumber=1
    )

    testResults = []

    # stack the tests below here
    testDict = {"lastName": "hoogmoed", "password": "jokers", "postcodePlusID": 4311240}
    try:
        testResults.append(
            test(
                exercise1.get_some_details() == testDict,
                "Exercise 1: get some data out of a JSON file",
            )
        )
    except Exception as e:
        testResults.append(test(False, "Exercise 1: get some data out of a JSON file"))

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
            "args": (1, 5),
            "result": {"name": "venusaur", "weight": 1000, "height": 20},
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
            testResults.append({"value": 0, "name": "Exercise 1: Consult the Pokedex."})
        except Exception as e:
            testResults.append({"value": 0, "name": "Exercise 1: Consult the Pokedex."})
            print(ex_name, e)

    try:
        testResults.append(
            test(find_lasers(path_to_code_to_check), "Exercise 1: count the lasers.")
        )
    except Exception as e:
        testResults.append(test(False, "Exercise 1: count the lasers."))

    message = "Rad, you've got all the tests passing!"

    return finish_up(testResults, message, nyan_cat())


def pokeball() -> str:
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


def tiny_pikachu() -> str:
    return r"""
/\︿╱\
\0_ 0 /╱\╱ 
\▁︹_/
    """


def pikachu() -> str:
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


def squirtle() -> str:
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
