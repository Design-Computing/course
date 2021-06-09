# -*- coding: UTF-8 -*-
"""Collect up the functons used in all the sets."""
import importlib.util as importUtils
import inspect
import os
import subprocess
import threading
import traceback
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import colorama
from colorama import Fore, Style

colorama.init()


class RunCmd(threading.Thread):
    """Run a subprocess command, if it exceeds the timeout kill it.

    (without mercy)
    """

    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = subprocess.Popen(self.cmd)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()  # use self.p.kill() if process needs a kill -9
            self.join()


def finish_up(testResults: List[dict], message: str, the_treat: str) -> Dict[str, int]:
    print("\n\nRESULTS:", testResults, "\n\n")
    try:
        total = sum([r["value"] for r in testResults])
        out_of = len(testResults)

        package = {"of_total": out_of, "mark": total, "results": testResults}
        if total == out_of and total > 0:
            print(the_treat)
            completion_message(message, len(message) + 2)
        else:
            print("Keep going champ!")
        print(f"{total}/{out_of} (passed/attempted)")
    except Exception as e:
        package = {
            "of_total": 0,
            "mark": 0,
            "results": f"{e}\nBen is a moron and is trying to append a zero instead of a dictionary",
        }
    return package


def test(testResult: bool, name: str) -> Dict:
    """Report on the test.

    Returns 1 and 0 so that the 1s can be summed to give a mark.
    """
    value = 0
    try:
        if testResult:
            print((f"{Fore.GREEN}✔ {name}{Style.RESET_ALL}"))
            value = 1
        else:
            print((f"{Fore.RED}✘ {name}{Style.RESET_ALL}"))
    except Exception as e:
        print(e)
        print((f"{Fore.RED}✘ {name}{Style.RESET_ALL}"))

    return {"value": value, "name": name}


def test_flake8(fileName: str) -> bool:
    """Check to see if the file at file_path is flake8 compliant."""
    test_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    files = [os.path.join(test_dir, fileName)]
    # Import the legacy API as flake8 3.0 currently has no official
    # public API - this has to be changed at some point.
    from flake8.api import legacy as flake8

    style_guide = flake8.get_style_guide()
    report = style_guide.check_files(files)

    if report.total_errors == 0:
        return True
    else:
        print(report.total_errors)
        return False


def test_pydocstyle(fileName, flags="-e") -> bool:
    """Check to see if the file at file_path is pydocstyle compliant."""
    getFrame = inspect.getfile(inspect.currentframe())
    absPath = os.path.abspath(getFrame)
    test_dir = os.path.dirname(absPath)

    file_path = os.path.join(test_dir, fileName)
    print(file_path)
    try:
        child = subprocess.Popen(
            ["pydocstyle", file_path, flags], stdout=subprocess.PIPE
        )
        streamdata = child.communicate()[0]
        print(("streamdata", streamdata))  # I don't know what streamdata is for
        rc = child.returncode
        print(("returncode", rc))
        if rc == 0:
            print("all good")
            return True
        elif rc is None:
            print("all good, I think")
            return True
        else:
            print((f"U haz docstring errorz {grumpy()}"))
            return False
    except Exception as e:
        print(("failed to doc check", e))
        return False


def lab_book_entry_completed(setNumber: int, repo_path: str) -> bool:
    lab_book = Path(os.path.join(repo_path, f"set{setNumber}/readme.md"))
    if lab_book.is_file():
        with open(lab_book, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            basic_lab_book_content = [
                "TODO: Reflect on what you learned this week and what is still unclear."
            ]
            lines_stripped = [l.strip() for l in lines if l.strip() != ""]
            if lines_stripped == basic_lab_book_content:
                return False
            elif lines:
                return True
    return False


def loadExerciseFile(repo_path: str, setNumber: int = 2, exerciseNumber: int = 0):
    path = os.path.join(repo_path, f"set{setNumber}", f"exercise{exerciseNumber}.py")
    spec = importUtils.spec_from_file_location("exercise0", path)
    ex = importUtils.module_from_spec(spec)
    spec.loader.exec_module(ex)
    return ex


def ex_runs(repo_path: str, setNumber: int = 2, exerciseNumber: int = 1) -> bool:
    """Check that this exercise runs at all."""
    try:
        p = os.path.normpath(
            os.path.join(repo_path, f"set{setNumber}/exercise{exerciseNumber}.py")
        )
        spec = importUtils.spec_from_file_location("exercise", p)
        ex = importUtils.module_from_spec(spec)
        spec.loader.exec_module(ex)
        return True
    except Exception as e:
        syntax_error_message(exerciseNumber, e)
        return False


def syntax_error_message(exerciseNumber: int, e) -> None:
    """Give a readable error message."""
    print("\n{s:{c}^{n}}\n{s:{c}^{n}}".format(n=50, c="*", s=""))
    print(f"There is a syntax error in exercise{exerciseNumber}\n{e}")
    print(traceback.print_exc())
    print("\nWARNING: there might be more tests, but they won't run")
    print(f"until you fix the syntax errors in exercise{exerciseNumber}.py")
    print("{s:{c}^{n}}\n{s:{c}^{n}}\n".format(n=50, c="*", s=""))


def completion_message(message, width) -> None:
    """Print an obvious message.

    Example:
    In [5]: completion_message("this is the message", 30)
    ******************************

    ✔ this is the message

    ******************************
    """
    cap = "{start}{s:{c}^{n}}{end}".format(
        n=width, c="*", s="", start=Fore.GREEN, end=Style.RESET_ALL
    )
    print(f"{cap}\n")
    print((f"{Fore.GREEN}✔ {message}{Style.RESET_ALL}"))
    print(f"\n{cap}")


def timeout_message(
    function_name: str = "unknown function name",
    args=(1, 2, 3),
    timeout_in_seconds: int = 5,
) -> None:
    print(
        f"{function_name}({args}) could not complete "
        f"within {timeout_in_seconds} seconds and was killed."
    )


def deadpool(message: str = "Good Job", name: str = "Dude") -> str:
    return """
                ▄▄▄▓▓▓▓▓▄▄▄
             ▄███████████████▄▄
           ▄████████████████████▄
          ████████████████████████▄
         ██████████▄███████▄▄▄██████
        ███████▀ ██████████████▄ ████
       ███████  █████████████████ ▀██▌
      ▐██████    ▀█████████████████ ▀█
      ██████ ▄▓▓▄ ▀████████████████
     ▐█████ ▓█████ ▀█████████████▀ ▄▓▓▌
     █████▌▐███████▄▀▀█████████▀▀▄████▓
    ▐█████ ███▀▀▀▀▀██▄▀▀█████▀ ▄███████
    ▐█████ ██ ▀▀▀▀▀ ███ ░▓▓▓░ ██▀▄▄▄▀█▌
     ▐████▌▐█▓▓▓▓▓███▀▄▄█░░░█▄▄▀▄▄▄▄▄█
      ▀████ ███████▀▄███████████▄▀▓▓▓▌       ▄▄▄▄▄▄▄▄▄
     ▓█▄▀██▌▐████▀▄█▓▓▓▓▓▓▓▓▓████▌ ▀▄     ▄████████████▄
     ▐███ ██ ▀▀▀ ██▓▓▓▓▓▓▓▓▓▓▓▓███ █     █{m}█
      ███████   ██▓▓██████████▓▓█▌█    ▄█{n}█
       ███████ ██▓█████████████▓▒█   ▄████████████████████
        ▀███████▓███████████████▓   █▀   ▀██████████████▀
          ▀████▐███████████████▀          ▀▓▓▓▓▓▓▓▓▓▓▀▀
         ██▄▀████████████████▀▀
       ▄████▄ ▀▀▀█████████▀▀
     ▄████████▄   ▀▀▀▀▀▀▀  ▄▄█
   ▀▓▓▓▓▓▓▓▓▓▓▓█▄      ▄▓▓▓▓▓
""".format(
        m=message.center(14, "█"), n=name.center(15, "█")
    )


def nyan_cat(block: str = "█") -> str:
    """Return a coloured string that shows a nyan cat."""
    c = [
        ["{BRIGHT_BLUE}", "{x}" * 80],
        ["{BRIGHT_BLUE}", "{x}" * 80],
        [
            "{RED}",
            "{x}" * 18,
            "{BRIGHT_BLUE}",
            "{x}" * 16,
            "{BLACK}",
            "{x}" * 30,
            "{BRIGHT_BLUE}",
            "{x}" * 16,
        ],
        [
            "{RED}",
            "{x}" * 32,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 30,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 14,
        ],
        [
            "{BRIGHT_RED}",
            "{x}" * 4,
            "{RED}",
            "{x}" * 26,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{MAGENTA}",
            "{x}" * 22,
            "{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        [
            "{BRIGHT_RED}",
            "{x}" * 30,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{MAGENTA}",
            "{x}" * 16,
            "{BLACK}",
            "{x}" * 4,
            "{MAGENTA}",
            "{x}" * 6,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{BRIGHT_BLUE}",
            "{x}" * 6,
        ],
        [
            "{BRIGHT_RED}",
            "{x}" * 30,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{MAGENTA}",
            "{x}" * 6,
            "{WHITE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_YELLOW}",
            "{x}" * 18,
            "{BRIGHT_RED}",
            "{x}" * 12,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{MAGENTA}",
            "{x}" * 6,
            "{WHITE}{x}{x}{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_YELLOW}",
            "{x}" * 22,
            "{BLACK}{x}{x}{BRIGHT_YELLOW}",
            "{x}" * 6,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 8,
            "{WHITE}",
            "{x}" * 8,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_YELLOW}",
            "{x}" * 20,
            "{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}{x}{x}{BRIGHT_YELLOW}",
            "{x}" * 4,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 22,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_GREEN}",
            "{x}" * 18,
            "{BRIGHT_YELLOW}{x}{x}{BLACK}",
            "{x}" * 2,
            "{WHITE}{x}{x}{BLACK}",
            "{x}" * 8,
            "{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 26,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BRIGHT_GREEN}",
            "{x}" * 22,
            "{WHITE}",
            "{x}" * 8,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BRIGHT_YELLOW}{x}{x}{WHITE}",
            "{x}" * 10,
            "{BRIGHT_YELLOW}{x}{x}{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BRIGHT_GREEN}",
            "{x}" * 22,
            "{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BLUE}",
            "{x}" * 18,
            "{BRIGHT_GREEN}",
            "{x}" * 8,
            "{BLACK}",
            "{x}" * 6,
            "{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 16,
            "{MAGENTA}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BLUE}",
            "{x}" * 30,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 12,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 18,
            "{BLUE}",
            "{x}" * 4,
            "{BLUE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 6,
            "{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 18,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 6,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 26,
            "{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 20,
            "{BLACK}",
            "{x}" * 18,
            "{BRIGHT_BLUE}",
            "{x}" * 8,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 24,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 32,
            "{WHITE}{x}{x}{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 24,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BRIGHT_BLUE}",
            "{x}" * 12,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 24,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 4,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 12,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 4,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        ["{x}" * 80, "{WHITE}"],
    ]
    c = "\n".join(["".join(x) for x in c])
    return c.format(
        BLACK=f"{Style.NORMAL}{Fore.BLACK}",
        BLUE=f"{Style.NORMAL}{Fore.BLUE}",
        BRIGHT_BLUE=f"{Style.BRIGHT}{Fore.BLUE}",
        BRIGHT_GREEN=f"{Style.BRIGHT}{Fore.GREEN}",
        BRIGHT_RED=f"{Style.BRIGHT}{Fore.RED}",
        BRIGHT_YELLOW=f"{Style.BRIGHT}{Fore.YELLOW}",
        MAGENTA=f"{Style.NORMAL}{Fore.MAGENTA}",
        RED=f"{Style.NORMAL}{Fore.RED}",
        WHITE=f"{Style.BRIGHT}{Fore.WHITE}",
        x=block,
    )


def grumpy() -> str:
    """Return a grumpy cat.

    from: http://textart4u.blogspot.com.au/
                 2013/02/grumpy-cat-meme-ascii-text-art.html
    """
    return """
▌▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   ▐█  ▀▀▀▐
▌    ▄                  ▄█▓█▌    ▐
▌   ▐██▄               ▄▓░░▓▓    ▐
▌   ▐█░██▓            ▓▓░░░▓▌    ▐
▌   ▐█▌░▓██          █▓░░░░▓     ▐
▌    ▓█▌░░▓█▄███████▄███▓░▓█     ▐
▌    ▓██▌░▓██░░░░░░░░░░▓█░▓▌     ▐
▌     ▓█████░░░░░░░░░░░░▓██      ▐
▌     ▓██▓░░░░░░░░░░░░░░░▓█      ▐
▌     ▐█▓░░░░░░█▓░░▓█░░░░▓█▌     ▐
▌     ▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌     ▐
▌     ▓▓░▓██████▓░▓███▓▓▌░█▓     ▐
▌    ▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██     ▐
▌    ▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌    ▐
▌    ▓█▌░▓█████▓░░░▓███▓▀░▓█▓    ▐
▌   ▐▓█░░░▀▓██▀░░░░░ ▀▓▀░░▓█▓    ▐
▌   ▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓    ▐
▌   ▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌   ▐
▌   ▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓   ▐
▌  ▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓▌  ▐
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░██▓  ▐
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓  ▐
██████████████████████████████████
█░▀░░░░▀█▀░░░░░░▀█░░░░░░▀█▀░░░░░▀█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░░░░░▄█░░▄▄▄▄▄█
█░░▐█▌░░█░░░██░░░█░░░░████░░░░░░░█
█░░▐█▌░░█▄░░░░░░▄█░░░░████▄░░░░░▄█
██████████████████████████████████"""


if __name__ == "__main__":
    pass
