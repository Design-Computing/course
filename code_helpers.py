# -*- coding: UTF-8 -*-
"""Collect up the functions used in all the sets."""
import getpass
import importlib.util as importUtils
import inspect
import json
import os
import subprocess
import threading
import traceback
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Union

import colorama
import pandas as pd
from colorama import Fore, Style

from treats import deadpool, grumpy, nyan_cat

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


def terse_results(results):
    s = ""
    for result in results:
        mark = "👍" if result.get("value") == 1 else "💩"
        s += f"{mark} {result.get('name','')}\n"
    return s


def finish_up(
    testResults: List[dict],
    message: str,
    the_treat: str,
    week_number: int = 0,
    path_to_save_trace_to: str = "../me",
    print_results_summary=True,
) -> Dict[str, Union[int, str, List[dict]]]:
    if print_results_summary:
        print(
            "\n\nResult summary:  (👆 scroll up for more details ☝)\n"
            + terse_results(testResults),
        )
    total = sum([r["value"] for r in testResults])
    out_of = len(testResults)

    package = {
        "of_total": out_of,
        "mark": total,
        "results": testResults,
        "week_number": week_number,
    }

    if total == out_of and total > 0:
        print(the_treat)
        completion_message(message, len(message) + 2)
    else:
        print("\nKeep going champ! 🌟✨🌟✨ I believe in you! 🌟✨🌟✨\n")
    print(f"{total}/{out_of} (passed/attempted)")

    if getpass.getuser() != "bdoherty":
        # TODO: what is this doing, and why do we need it?
        # os.getlogin() != "bdoherty":
        write_results(package, week_number, path_to_save_trace_to)

    return package


def write_results(
    package: Dict[str, Union[int, str, List[dict]]],
    week_number: int = 0,
    path_to_save_trace_to: str = "../me",
) -> None:
    trace: str = ""
    tracefile = os.path.join(path_to_save_trace_to, "trace.json")
    if os.path.isfile(tracefile):
        with open(tracefile, "r", encoding="utf-8") as f:
            trace = json.load(f)
            trace[week_number - 1] = package
        with open(tracefile, "w", encoding="utf-8") as f:
            json.dump(trace, f, indent=2)
    else:
        with open(tracefile, "w", encoding="utf-8") as f:
            trace = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            trace[week_number] = package
            json.dump(trace, f, indent=2)


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


def load_exercise_file(repo_path: str, setNumber: int = 2, exerciseNumber: int = 0):
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
        spec = importUtils.spec_from_file_location("exercise", os.path.abspath(p))
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


def print_timeout_message(
    function_name: str = "unknown function name",
    args=(1, 2, 3),
    timeout_in_seconds: int = 5,
) -> None:
    """Print a message to explain to the user that their function didn't complete in the available time.

    The message looks like:
        do_stuff ([2, "tree", {"k", "v"}]) could not complete within 5 seconds and was killed.

    Args:
        function_name (str, optional): the name of the function. Defaults to "unknown function name".
        args (tuple, optional): the args passed to the function. Defaults to (1, 2, 3).
        timeout_in_seconds (int, optional): Time in seconds available to complete. Defaults to 5.
    """
    print(
        f"{function_name}({args}) could not complete "
        f"within {timeout_in_seconds} seconds and was killed."
    )


if __name__ == "__main__":
    print(
        "you probably meant to run something else, not this collection of helper files"
    )
