"""Do the work of checking the week's work."""

import sys
import os
import inspect
from pathlib import Path
from colorama import Fore
from colorama import Style

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from codeHelpers import (
    completion_message,
    ex_runs,
    lab_book_entry_completed,
    loadExerciseFile,
    nyan_cat,
    test,
    test_flake8,
)


# from codeHelpers import test
# from week1 import exercise1

WEEK_NUMBER = 1
ME = "../me"
EM = Fore.YELLOW
NORM = Fore.WHITE

# the context of this file
sys.path.append("../me/week{}".format(WEEK_NUMBER))

testResults = []


def test_hello_world():
    exercise1 = loadExerciseFile(weekNumber=WEEK_NUMBER, exerciseNumber=1)
    source = "".join(inspect.getsourcelines(exercise1)[0])
    if (
        "print('hello world!')" in source.lower()
        or 'print("hello world!")' in source.lower()
    ):
        return True

    print(
        """
We're looking for:

{em}print(\"hello world!\"){norm}

but your code is \n{sep}\n{em}{code}{norm}\n{sep}
Look carefully at your capitalisation, 
spelling, brackets, spaces etc.""".format(
            code=source, sep="═" * 80, em=EM, norm=NORM
        )
    )

    return False


def test_dev_env():
    if os.system("""python -c 'print("python installed")'""") == 0:
        return True
    else:
        print(
            "Python doesn't seem to be installed properly on your computer.\n"
            "Have you installed Anaconda?\n"
            "Have you restarted your computer?\n"
            "Talk to a tutor and get them to help you out."
        )
    return False


if __name__ == "__main__":
    testResults.append(
        test(test_dev_env(), "Python is installed and configured on this machine")
    )
    testResults.append(test(test_hello_world(), "Exercise1: Print 'Hello world!'"))
    testResults.append(test(lab_book_entry_completed(1), "Lab book entry completed"))
