"""Do the work of checking the week's work."""

from colorama import Fore
from colorama import Style
from pathlib import Path
import git
import inspect
import json
import os
import ruamel.yaml as yaml
import sys
import systemCheck
import requests

REMOTE = "../me/week1"
aboutMeData = ""

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from codeHelpers import (
    completion_message,
    ex_runs,
    lab_book_entry_completed,
    loadExerciseFile,
    nyan_cat,
    test,
    test_flake8,
    deadpool,
)


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


def test_aboutMe(show=False):
    """Test to see if aboutMe.yml is updated"""
    f = open("../me/aboutMe.yml", "r")
    them = dict(yaml.load(f, yaml.RoundTripLoader))
    global aboutMeData
    aboutMeData = them
    if show:
        print(json.dumps(them, indent=2, sort_keys=True))
    if (
        them["name"] == "Your Name"
        or them["name"] == "Your Name"
        or them["studentNumber"] == "z1234567"
        or them["officialEmail"] == "noIdea@unsw.edu.au"
    ):
        return False
    else:
        return True


def me_repo_is_clone():
    try:
        repo = git.cmd.Git("../me")
        origin_url = repo.execute("git config --get remote.origin.url")
        if "Design-Computing" in origin_url:
            print(
                (
                    "You seem to be running on the master copy of the {em}me{norm} repo."
                    "\nYou need to be working with your clone."
                    "\nThis is hard to explain in an error message, call a tutor over."
                ).format(em=EM, norm=NORM)
            )
            return False
        else:
            return True
    except Exception as e:
        print("TODO: write an error message here", e)
        return False


def has_pushed(fileName):
    try:
        repo = git.cmd.Git("../me")
        origin_url = repo.execute("git config --get remote.origin.url")
        owner = origin_url.split("/")[3]
        url = "https://api.github.com/repos/" + "{o}/me/contents/week1/{f}".format(
            o=owner, f=fileName
        )
        r = requests.get(url)
        if r.status_code == 404:
            print("Have you pushed yet?")
            return False
        else:
            return True
    except Exception as e:
        print("TODO: write an error message here", e)
        return False


if __name__ == "__main__":
    testResults.append(
        test(systemCheck.check_system_details(), "Run a trace on your system details")
    )
    testResults.append(
        test(
            systemCheck.test_for_python_and_requests(),
            "check that Python and Requests are installed",
        )
    )
    testResults.append(
        test(test_dev_env(), "Python is installed and configured on this machine")
    )
    testResults.append(test(test_hello_world(), "Exercise1: Print 'Hello world!'"))
    testResults.append(test(lab_book_entry_completed(1), "Lab book entry completed"))
    about_me_filled_in = test_aboutMe()
    testResults.append(test(about_me_filled_in, "Update your aboutMe.yml"))
    if about_me_filled_in is False:
        test_aboutMe(show=True)
        print(
            "This is your aboutMe.yml file (but shown as JSON)",
            "You need to update it to have your real information,",
            "or we can't give you any marks",
        )

    f = "requestsWorking.txt"
    testResults.append(
        test(os.path.isfile(os.path.join("..", "me", "week1", f)), f + " exists")
    )

    f = "checkID.json"
    testResults.append(
        test(os.path.isfile(os.path.join("..", "me", "week1", f)), f + " exists")
    )

    testResults.append(test(me_repo_is_clone(), "You've forked the me repo"))

    f = "requestsWorking.txt"
    testResults.append(test(has_pushed(f), "You've pushed your work to GitHub: " + f))
    f = "checkID.json"
    testResults.append(test(has_pushed(f), "You've pushed your work to GitHub: " + f))

    print(
        {"of_total": len(testResults), "mark": sum(testResults), "results": testResults}
    )

    if len(testResults) == sum(testResults):
        name = aboutMeData["name"].split(" ")[0]
        deadpool("Good Job", name)
    else:
        print(
            """
How To Read this
----------------

The results part shows a list of the marks, either 1 or 0. 
There are no partial marks, it either works or it doesn't.
Each test accounts for 1 mark, so the "mark" is the total of that list.
"of_total" is the number of tests performed.
You are, of course, aiming for these two numbers to be the same!

Don't forget to commit AND push!

The last 2 tests will run on your machine because you've just made those files.
However, they won't run on the marking computer if they haven't been pushed to your repo. 

Type {em}git status{norm}, or look in your source control tab, to check.
""".format(
                em=EM, norm=NORM
            )
        )
