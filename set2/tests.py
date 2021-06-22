# -*- coding: UTF-8 -*-
"""Run the tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

# TODO replace flake8 with yapf or calm flake8 down

import importlib.util as importUtils
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from colorama import Fore, Style

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

SET_NUMBER = 2

sys.path.append(f"../me/set{SET_NUMBER}")


def theTests(path_to_code_to_check="../me") -> dict:
    """Run the tests."""
    print(f"\nWelcome to set {SET_NUMBER}!\n")
    print("May the odds be ever in your favour.\n")

    testResults = []

    # Tests from here:

    if ex_runs(path_to_code_to_check, exerciseNumber=0, setNumber=SET_NUMBER):
        exercise0 = loadExerciseFile(
            path_to_code_to_check, setNumber=SET_NUMBER, exerciseNumber=0
        )

        testResults.append(
            test(exercise0.add_1(55) == 56, "Exercise 0: add_1 - 55 + 1 = 56")
        )
        testResults.append(
            test(exercise0.add_1(-5) == -4, "Exercise 0: add_1 - -5 + 1 = -4")
        )
        testResults.append(
            test(exercise0.add_1(0.1) == 1.1, "Exercise 0: add_1 - 0.1 + 1 = 1.1")
        )

        testResults.append(
            test(exercise0.add_5(55) == 60, "Exercise 0: add_5 - 55 + 5 = 60")
        )
        testResults.append(
            test(exercise0.add_5(-5) == 0, "Exercise 0: add_5 - -5 + 5 = 0")
        )
        testResults.append(
            test(exercise0.add_5(0.1) == 5.1, "Exercise 0: add_5 - 0.1 + 5 = 5.1")
        )

        testResults.append(
            test(exercise0.adder(5, 5) == 10, "Exercise 0: adder - 5 + 5 = 10")
        )
        testResults.append(
            test(exercise0.adder(-5, -5) == -10, "Exercise 0: adder - -5 + -5 = -10")
        )
        testResults.append(
            test(exercise0.adder(0.1, 0.9) == 1, "Exercise 0: adder - 0.1 + 0.9 = 1")
        )

        words = "you've got to fight for your right to party".split(" ")
        for word in words:
            word_up = word.upper()
            testResults.append(
                test(
                    exercise0.shout(word) == word_up,
                    f"Exercise 0: shout - {word} => {word_up}",
                )
            )

        testResults.append(
            test(
                exercise0.shout_with_a_number("hi", 1) == "HI 1",
                "Exercise 0: shout_with_a_number - hi, 1 => HI 1",
            )
        )

    ex2_runs = ex_runs(path_to_code_to_check, exerciseNumber=2, setNumber=SET_NUMBER)

    if not ex2_runs:
        print("Don't worry, exercise 2 comes with errors. It's your job to fix them!")
    testResults.append(test(ex2_runs, "Exercise 2: debug the file"))

    if ex_runs(path_to_code_to_check, exerciseNumber=3, setNumber=SET_NUMBER):
        exercise3 = loadExerciseFile(
            path_to_code_to_check, setNumber=SET_NUMBER, exerciseNumber=3
        )
        # is odd
        testResults.append(
            test(exercise3.is_odd(2) is False, "Exercise 3: is_odd - is 2 odd")
        )

        testResults.append(test(exercise3.is_odd(5), "Exercise 3: is_odd - is 5 odd"))

        # fix it
        scenarios = [
            {"it_moves": True, "it_should_move": True, "answer": "No Problem"},
            {"it_moves": True, "it_should_move": False, "answer": "Duct Tape"},
            {"it_moves": False, "it_should_move": True, "answer": "WD-40"},
            {"it_moves": False, "it_should_move": False, "answer": "No Problem"},
        ]
        for s in scenarios:
            it = "moves" if s["it_moves"] else "does not move"
            should = "" if s["it_should_move"] else "not"
            result = exercise3.fix_it(s["it_moves"], s["it_should_move"]) == s["answer"]
            if not result:
                print(
                    f"""Trying it {it} and it {should} move """
                    f"""and we're getting {exercise3.fix_it(s["it_moves"], s["it_should_move"])}.\n"""
                    f"""We should be getting {s["answer"]}."""
                )
            testResults.append(
                test(
                    result,
                    f"Exercise 3: fix_it - it {it}, and it should {should} move",
                )
            )

        # loops
        tenStars = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        result = exercise3.loops_1a()
        if result == tenStars:
            testResults.append(test(True, "Exercise 3: loops_1a - 1d for loop"))
        else:
            print(
                f"{NORM}"
                f"You're returning:  {EM}{result}{NORM}. "
                f"We're looking for: {EM}{tenStars}{NORM}"
            )
            if result == None:
                print(
                    (
                        "{norm}Do you have a line that says "
                        "{em}return the_answer{norm}?\n"
                        "Or maybe you have a line that says {em}return None{norm}?"
                        "Or you are returning a variable that has the value "
                        "{em}return None{norm}?\n"
                        "Remember: {em}return print(something){norm} is the same "
                        "as {em}return None{norm} because {em}print{norm} returns "
                        "None\n"
                        "You need to return the computed value, so either assign "
                        "it to a variable and return that, or return it directly."
                    ).format(em=EM, norm=NORM)
                )
            elif result == "**********":
                print("remember that we're looking for a list")
            # TODO: write more failure modes as they come up in testing.

        testResults.append(
            test(
                exercise3.loops_1c(3, ":)") == [":)", ":)", ":)"],
                "Exercise 3: loops_1c - 1d with arguments",
            )
        )

        ten_by_ten_stars = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ]
        testResults.append(
            test(
                exercise3.loops_2() == ten_by_ten_stars,
                "Exercise 3: loops_2 - 10×10 stars",
            )
        )

        ten_matching_numbers = [
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"],
            ["3", "3", "3", "3", "3", "3", "3", "3", "3", "3"],
            ["4", "4", "4", "4", "4", "4", "4", "4", "4", "4"],
            ["5", "5", "5", "5", "5", "5", "5", "5", "5", "5"],
            ["6", "6", "6", "6", "6", "6", "6", "6", "6", "6"],
            ["7", "7", "7", "7", "7", "7", "7", "7", "7", "7"],
            ["8", "8", "8", "8", "8", "8", "8", "8", "8", "8"],
            ["9", "9", "9", "9", "9", "9", "9", "9", "9", "9"],
        ]
        testResults.append(
            test(
                exercise3.loops_3() == ten_matching_numbers,
                "Exercise 3: loops_3 - 10 matching lists",
            )
        )

        ten_rising_lists = [
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ]
        res = exercise3.loops_4()
        if res == ten_rising_lists:
            testResults.append(test(True, "Exercise 3: loops_4 - ten rising lists"))
        elif res is None:
            print("Still returning None")
            testResults.append(test(False, "Exercise 3: loops_4 - ten rising lists"))
        elif len(res) == 10 and res[0][0] == 0:
            print(
                "This is looking promising, but the test is looking for "
                "strings, not numbers. look into what str() does"
            )
            testResults.append(test(False, "Exercise 3: loops_4 - ten rising lists"))
        else:
            print(
                f"You're giving us:\n{res}\nbut we're looking for\n{ten_rising_lists}\n"
                "Can you see a difference? What is it?"
            )
            testResults.append(test(False, "Exercise 3: loops_4 - ten rising lists"))

        coords = [
            ["(i0, j0)", "(i0, j1)", "(i0, j2)", "(i0, j3)", "(i0, j4)"],
            ["(i1, j0)", "(i1, j1)", "(i1, j2)", "(i1, j3)", "(i1, j4)"],
            ["(i2, j0)", "(i2, j1)", "(i2, j2)", "(i2, j3)", "(i2, j4)"],
            ["(i3, j0)", "(i3, j1)", "(i3, j2)", "(i3, j3)", "(i3, j4)"],
            ["(i4, j0)", "(i4, j1)", "(i4, j2)", "(i4, j3)", "(i4, j4)"],
            ["(i5, j0)", "(i5, j1)", "(i5, j2)", "(i5, j3)", "(i5, j4)"],
            ["(i6, j0)", "(i6, j1)", "(i6, j2)", "(i6, j3)", "(i6, j4)"],
            ["(i7, j0)", "(i7, j1)", "(i7, j2)", "(i7, j3)", "(i7, j4)"],
            ["(i8, j0)", "(i8, j1)", "(i8, j2)", "(i8, j3)", "(i8, j4)"],
            ["(i9, j0)", "(i9, j1)", "(i9, j2)", "(i9, j3)", "(i9, j4)"],
        ]
        testResults.append(
            test(
                exercise3.loops_5() == coords, "Exercise 3: loops_5 - write the coords"
            )
        )

        wedge = [
            ["0"],
            ["0", "1"],
            ["0", "1", "2"],
            ["0", "1", "2", "3"],
            ["0", "1", "2", "3", "4"],
            ["0", "1", "2", "3", "4", "5"],
            ["0", "1", "2", "3", "4", "5", "6"],
            ["0", "1", "2", "3", "4", "5", "6", "7"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ]
        testResults.append(
            test(exercise3.loops_6() == wedge, "Exercise 3: loops_6 - make a wedge")
        )

        pyramid = [
            [" ", " ", " ", " ", "*", " ", " ", " ", " "],
            [" ", " ", " ", "*", "*", "*", " ", " ", " "],
            [" ", " ", "*", "*", "*", "*", "*", " ", " "],
            [" ", "*", "*", "*", "*", "*", "*", "*", " "],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ]
        testResults.append(
            test(
                exercise3.loops_7() == pyramid, "Exercise 3: loops_7 - pyramid of stars"
            )
        )
    testResults.append(
        test(
            lab_book_entry_completed(SET_NUMBER, path_to_code_to_check),
            "Lab book entry completed",
        )
    )

    message = "Rad, you've got all the tests passing!"

    return finish_up(testResults, message, nyan_cat())


if __name__ == "__main__":
    theTests()  # no arg, runs tests on local code
