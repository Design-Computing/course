"""Do the work of checking the set's work."""

import inspect
import json
import os
import platform
import sys
from pathlib import Path

import git
import requests
import ruamel.yaml as yaml
from colorama import Fore, Style
from PIL import Image

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

SET_NUMBER = 1
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
    with open(os.path.join(repo_path, "set1", "checkID.json"), "w") as f:
        f.write(json.dumps(systemInfo, indent=4))

    return True


def test_for_python_and_requests(repo_path: str) -> bool:
    """Inspect own filesystem.

    GETs a small JSON file and displays a message
    """
    width: int = 38

    gh_url = "https://raw.githubusercontent.com/"
    check_repo = "notionparallax/code1161base/"
    file_path = f"master/week{SET_NUMBER}/pySuccessMessage.json"
    url = f"{gh_url}{check_repo}{file_path}"

    try:
        r = requests.get(url)
        message = json.loads(r.text)["message"]
        subMessage = "All hail his noodly appendage!"
    except Exception as e:
        message = "We are in the darkness"
        subMessage = "Alas, all is lost"
        print("\nThe error message:", e)

    boundary_char = "🍝"
    bar = f"{boundary_char}" * (int(width / 2) + 2)
    blank = "{b}{s:{c}^{n}}{b}".format(n=width, c=" ", s="", b=boundary_char)
    doesItWork = [
        bar,
        blank,
        "{b}{s:{c}^{n}}{b}".format(n=width, c=" ", s=message, b=boundary_char),
        blank,
        "{b}{s:{c}^{n}}{b}".format(n=width, c=" ", s=subMessage, b=boundary_char),
        blank,
        bar,
    ]

    print("Let's test Python and Requests:\n")
    for line in doesItWork:
        print(line)

    p = os.path.join(repo_path, f"set{SET_NUMBER}", "requestsWorking.txt")
    with open(p, "w", encoding="utf-8") as f:
        for line in doesItWork:
            f.write(f"{line}\n")

    return True


def test_hello_world(repo_path: str) -> bool:
    exercise1 = loadExerciseFile(repo_path, setNumber=SET_NUMBER, exerciseNumber=1)
    source = "".join(inspect.getsourcelines(exercise1)[0])
    if "print('Hello world!')" in source or 'print("Hello world!")':
        print("that's exactly right!, nice one.")
        return True
    if (
        # TODO: probably get a regex in here
        "print('hello world!')" in source.lower()
        or 'print("hello world!")' in source.lower()
        or 'print ("hello world!")' in source.lower()
        or "print ('hello world!')" in source.lower()
    ):
        print(
            "This is close enough, it passes, but it's not "
            "EXACTLY right, and sometimes it really matters "
            "what you write. Be pedantic!"
        )
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


# def str_dict_vals(d):
#     if hasattr(d, "keys"):
#         for k in d:
#             if hasattr(d[k], "keys"):
#                 str_dict_vals(dict(d[k]))
#             else:
#                 d[k] = str(d[k])
#         return dict(d)
#     else:
#         return d


def test_aboutMe(repo_path, show=False) -> bool:
    """Test to see if aboutMe.yml is updated"""
    file_path = os.path.join(repo_path, "aboutMe.yml")
    if not os.path.isfile(file_path):
        print(
            "this is very strange, have you deleted "
            "aboutMe.yml or renamed is? Don't do that!"
        )
        return False
    f = open(file_path, "r", encoding="utf8", errors="ignore")
    them = yaml.load(f, yaml.RoundTripLoader)
    # them = str_dict_vals(yaml.load(f, yaml.RoundTripLoader))
    global aboutMeData
    aboutMeData = them
    if show:
        print(json.dumps(them, indent=2, sort_keys=True))
    xx = "a very unexpected string"
    checks = [
        them.get("name", xx) == "Your Name",
        them.get("studentNumber", xx) == "z1234567",
        them.get("officialEmail", xx) == "noIdea@unsw.edu.au",
        "1835727/ben" in them.get("stackOverflowLink", xx),
        them.get("github", xx) == "notionparallax",
    ]
    if any(checks):
        print("You haven't updated all of your aboutMe.yml yet.")
        return False
    if all(checks):
        print("you haven't started on your aboutMe.yml yet.")
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
                "You seem to be running on the source copy of the {em}me{norm} repo."
                "\nIt looks like you've cloned {em}design-computing/me{norm}"
                "\nyou should have cloned {em}[your_github_name]/me{norm}"
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
        url = f"https://api.github.com/repos/{owner}/me/contents/set{SET_NUMBER}/{fileName}"
        r = requests.get(url)
        if r.status_code == 404:
            print("Have you pushed yet?")
            return False
        else:
            return True
    except Exception as e:
        print("TODO: write an error message here", e)
        return False


def has_real_photo(repo_path):
    repo = git.cmd.Git(repo_path)
    origin_url = get_origin_url(repo)
    owner = origin_url.split("/")[3]
    image_url = f"https://github.com/{owner}.png?size=40"
    img_data = requests.get(image_url).content
    file_name = "avatar.jpg"
    with open(file_name, "wb") as handler:
        handler.write(img_data)

    image = Image.open(file_name)
    colour_count = len(set(image.getdata()))

    if colour_count > 10:
        im = image.convert("P", palette=Image.ADAPTIVE, colors=9)
        block_image = blocky_photo(im, width=40)
        print(block_image)
        ret_val = True
    else:
        block_image = blocky_photo(image)
        print(
            f"Your GitHub profile picture only has {colour_count} colours.\n"
            "This makes me think it's the default avatar.\n"
            "Not like this:\n",
            block_image,
            """Like this:
╭───────────╮
│  !!!!!!!  │
│ /       \ │
│ │  O  O │ │  ⇇ where this is a photo of your face, of course!
│<│    v  │>│
│  \  ─── / │
│   \____/  │
╰───────────╯\n"""
            "Go to https://github.com/settings/profile and upload a photo of your face.\n"
            "This really helps us understand who's who and be more useful in tutorials.",
        )
        ret_val = False

    os.remove(file_name)
    return ret_val


def blocky_photo(image, width=20):
    colour_map_list = list(
        zip(
            list(set(image.getdata())),
            ["█", "░", "▒", "▓", "X", "#", "%", "/", ":", "*"],
        )
    )
    colour_map = {x[0]: x[1] for x in colour_map_list}
    image = image.resize((width, int(width / 2)), Image.NEAREST)
    pixels = list(image.getdata())
    width, height = image.size
    block_image = ""
    for i in range(len(pixels)):
        block_image += colour_map[pixels[i]]
        if (i + 1) % (width) == 0:
            block_image += "\n "
    return block_image


def theTests(path_to_code_to_check="../me") -> dict:
    """Run the tests."""
    print("checking:    ", path_to_code_to_check)
    print(f"\nWelcome to set {SET_NUMBER}!")
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
    p = os.path.join(path_to_code_to_check, f"set{SET_NUMBER}", f)
    testResults.append(test(os.path.isfile(p), f"{f} exists"))

    f = "checkID.json"
    p = os.path.join(path_to_code_to_check, f"set{SET_NUMBER}", f)
    testResults.append(test(os.path.isfile(p), f"{f} exists"))

    testResults.append(
        test(me_repo_is_clone(path_to_code_to_check), "You've forked the me repo")
    )

    f = "requestsWorking.txt"
    testResults.append(
        test(
            has_pushed(f, path_to_code_to_check),
            f"You've pushed your work to GitHub: {f}",
        )
    )
    f = "checkID.json"
    testResults.append(
        test(
            has_pushed(f, path_to_code_to_check),
            f"You've pushed your work to GitHub: {f}",
        )
    )

    testResults.append(
        test(
            has_real_photo(path_to_code_to_check),
            "You've got a photo for your GitHub account",
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
    treat = deadpool("Good Job", name)
    return finish_up(testResults, message, treat)


if __name__ == "__main__":
    theTests()
