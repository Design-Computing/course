"""Do the work of checking the week's work."""

from colorama import Fore
from colorama import Style
from pathlib import Path
import git
import inspect
import json
import os
import platform
import requests
import ruamel.yaml as yaml
import sys


aboutMeData = ""

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from codeHelpers import (
    completion_message,
    deadpool,
    ex_runs,
    finish_up,
    lab_book_entry_completed,
    loadExerciseFile,
    nyan_cat,
    test,
    test_flake8,
)


WEEK_NUMBER = 1
EM = Fore.YELLOW
NORM = Fore.WHITE

testResults = []


def check_system_details(repo_path: str) -> bool:
    """Look inside yourself.

    Gets the system details to check that this machine is actually set up
    """

    systemInfo = {
        "architecture": platform.architecture(),
        "machine": platform.machine(),
        "os_name": os.name,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "release": platform.release(),
        "system": platform.system(),
        "uname": platform.uname(),
        "version": platform.version(),
        "python_build": platform.python_build(),
        "python_compiler": platform.python_compiler(),
        "python_implementation(": platform.python_implementation(),
        "python_version(": platform.python_version(),
        "python_version_tuple": platform.python_version_tuple(),
        "cpu_count": os.cpu_count(),
    }
    print(json.dumps(systemInfo, indent=4))

    # Write it to a file in this repo
    f = open(os.path.join(repo_path, "week1", "checkID.json"), "w")
    f.write(json.dumps(systemInfo, indent=4))
    f.close()
    return True


def test_for_python_and_requests(repo_path: str) -> bool:
    """Inspect own filesystem.

    GETs a small JSON file and displays a message
    """
    width: int = 38

    gh_url = "https://raw.githubusercontent.com/"
    check_repo = "notionparallax/code1161base/"
    file_path = "master/week1/pySuccessMessage.json"
    url = gh_url + check_repo + file_path

    try:
        r = requests.get(url)
        message = json.loads(r.text)["message"]
        subMessage = "All hail his noodly appendage!"
    except Exception as e:
        message = "We are in the darkness"
        subMessage = "Alas, all is lost"
        print("\nThe error message:", e)

    bar = "*{s:{c}^{n}}*".format(n=width, c="*", s="")
    blank = "*{s:{c}^{n}}*".format(n=width, c=" ", s="")
    doesItWork = [
        bar,
        blank,
        "*{s:{c}^{n}}*".format(n=width, c=" ", s=message),
        blank,
        "*{s:{c}^{n}}*".format(n=width, c=" ", s=subMessage),
        blank,
        bar,
    ]

    print("Let's test Python and Requests:\n")
    for line in doesItWork:
        print(line)

    p = os.path.join(repo_path, "week1", "requestsWorking.txt")
    f = open(p, "w")
    for line in doesItWork:
        f.write(line + "\n")
    f.close()
    return True


def test_hello_world(repo_path: str) -> bool:
    exercise1 = loadExerciseFile(repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=1)
    source = "".join(inspect.getsourcelines(exercise1)[0])
    if (
        "print('hello world!')" in source.lower()
        or 'print("hello world!")' in source.lower()
    ):
        return True
    else:
        print(
            """
We're looking for:

{em}print(\"Hello world!\"){norm}

but your code is \n{sep}\n{em}{code}{norm}\n{sep}
Look carefully at your capitalisation, 
spelling, brackets, spaces etc.""".format(
                code=source, sep="═" * 80, em=EM, norm=NORM
            )
        )

        return False


def test_dev_env() -> bool:
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


def test_aboutMe(repo_path, show=False) -> bool:
    """Test to see if aboutMe.yml is updated"""
    f = open(os.path.join(repo_path, "aboutMe.yml"), "r")
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


def get_origin_url(repo) -> str:
    if os.name == "posix":
        return os.popen("git config --get remote.origin.url").read()
    else:
        return repo.execute("git config --get remote.origin.url")


def me_repo_is_clone(repo_path) -> bool:
    origin_url = ""
    try:
        repo = git.cmd.Git(repo_path)
        origin_url = get_origin_url(repo)
    except Exception as e:
        print("TODO: write an error message here", e)
        return False
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


def has_pushed(fileName, repo_path) -> bool:
    try:
        repo = git.cmd.Git(repo_path)
        origin_url = get_origin_url(repo)
        owner = origin_url.split("/")[3]
        url = f"https://api.github.com/repos/{owner}/me/contents/week1/{fileName}"
        r = requests.get(url)
        if r.status_code == 404:
            print("Have you pushed yet?")
            return False
        else:
            return True
    except Exception as e:
        print("TODO: write an error message here", e)
        return False


def theTests(path_to_code_to_check="../me") -> dict:
    """Run the tests."""
    print("checking:    ", path_to_code_to_check)
    print(f"\nWelcome to week {WEEK_NUMBER}!")
    print("May the odds be ever in your favour.\n")

    testResults = []
    testResults.append(
        test(
            check_system_details(path_to_code_to_check),
            "Run a trace on your system details",
        )
    )
    testResults.append(
        test(
            test_for_python_and_requests(path_to_code_to_check),
            "check that Python and Requests are installed",
        )
    )
    testResults.append(
        test(test_dev_env(), "Python is installed and configured on this machine")
    )
    testResults.append(
        test(test_hello_world(path_to_code_to_check), "Exercise1: Print 'Hello world!'")
    )
    testResults.append(
        test(
            lab_book_entry_completed(1, path_to_code_to_check),
            "Lab book entry completed",
        )
    )
    about_me_filled_in = test_aboutMe(path_to_code_to_check)
    testResults.append(test(about_me_filled_in, "Update your aboutMe.yml"))
    if about_me_filled_in is False:
        test_aboutMe(path_to_code_to_check, show=True)
        print(
            "This is your aboutMe.yml file (but shown as JSON)",
            "You need to update it to have your real information,",
            "or we can't give you any marks",
        )

    f = "requestsWorking.txt"
    p = os.path.join(path_to_code_to_check, "week1", f)
    testResults.append(test(os.path.isfile(p), f + " exists"))

    f = "checkID.json"
    p = os.path.join(path_to_code_to_check, "week1", f)
    testResults.append(test(os.path.isfile(p), f + " exists"))

    testResults.append(
        test(me_repo_is_clone(path_to_code_to_check), "You've forked the me repo")
    )

    f = "requestsWorking.txt"
    testResults.append(
        test(
            has_pushed(f, path_to_code_to_check),
            "You've pushed your work to GitHub: " + f,
        )
    )
    f = "checkID.json"
    testResults.append(
        test(
            has_pushed(f, path_to_code_to_check),
            "You've pushed your work to GitHub: " + f,
        )
    )

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

    name = aboutMeData["name"].split(" ")[0]
    message = "Rad, you've got all the tests passing!"
    return finish_up(testResults, message, deadpool("Good Job", name))


if __name__ == "__main__":
    theTests()
