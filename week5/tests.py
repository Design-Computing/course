# -*- coding: UTF-8 -*-
"""Test week 5's code.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

# from datetime import datetime
# import math
# import requests
# import time
from colorama import Fore
from colorama import Style
from pathlib import Path
import importlib.util as importUtils
import inspect
import io
import os
import sys
from typing import List, Set, Dict, Tuple, Optional

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import (
    completion_message,
    ex_runs,
    finish_up,
    grumpy,
    lab_book_entry_completed,
    loadExerciseFile,
    nyan_cat,
    test,
    test_flake8,
    test_pydocstyle,
)

EM = Fore.YELLOW
NORM = Fore.WHITE

WEEK_NUMBER = 5
PASS = 1
FAIL = 0
LOCAL = os.path.dirname(os.path.realpath(__file__))

if "week" in os.getcwd():
    os.chdir("..")


def test_diagrams(diagram, expected) -> bool:
    """Test, crudely, that the correct diagram is being returned."""
    # print("testing", diagram, expected)
    if diagram and expected:
        if expected == "tall" and ("\\" in diagram):
            return True
        if expected == "wide" and "∕" in diagram:
            return True
        if expected == "equal" and "⋱" in diagram:
            return True
    print("failure in test_diagrams", "\n", grumpy())
    return False


def test_word_length(word: str, requested_length, expected_length) -> bool:
    """Check that word lenths are as expected.

    Requesting a word less than 3 chars long should fail.
    """
    print(
        f"testing: word:{word}, "
        f"requested_length:{requested_length}, "
        f"expected_length:{expected_length}"
    )
    if type(requested_length) is str and word is not None:
        print(
            "This API returns a random word if you malform the url\n",
            "You'll need to typecheck the input. I.e. check\n",
            "if type(length) is int:\n",
            "....#and so on\n",
            "It also does the same thing if you go under 3 characters\n",
            "long, so remember to check for that too!",
        )
        print(grumpy())
    if expected_length is None and word is None:
        return True
    if word is None:
        return False
    if len(word) == requested_length and len(word) == expected_length:
        return True
    print("Something a bit odd is happening")
    print(grumpy())
    return False


def theTests(path_to_code_to_check="..\me") -> dict:
    """Run the tests."""
    print(f"\nWelcome to week {WEEK_NUMBER}!")
    print("May the odds be ever in your favour.\n")

    testResults = []

    # stack the tests below here
    path = f"{path_to_code_to_check}/week{WEEK_NUMBER}/exercise1.py"
    print(path)

    exercise1 = loadExerciseFile(
        path_to_code_to_check, weekNumber=WEEK_NUMBER, exerciseNumber=1
    )

    # Linter test
    # print("Linter test:", path)
    # testResults.append(
    #     test(test_flake8(path),
    #          "Exercise 1: pass the linter"))

    # pydocstyle test
    # print("Docstyle test:", path)
    # testResults.append(
    #     test(test_pydocstyle(path),
    #          "Exercise 1: pass the pydocstyle test"))

    # countdown test
    book_of_counts = [
        {
            "expect": """let's get ready to rumble 8
let's get ready to rumble 7
let's get ready to rumble 6
let's get ready to rumble 5
let's get ready to rumble 4
let's get ready to rumble 3
let's get ready to rumble 2
let's get ready to rumble 1
*rumbling sound*
""",
            "input": {
                "message": "let's get ready to rumble",
                "start": 8,
                "stop": 1,
                "completion_message": "*rumbling sound*",
            },
        },
        {
            "expect": """prepare to die in this many ways: 5
prepare to die in this many ways: 4
prepare to die in this many ways: 3
prepare to die in this many ways: 2
or not, I guess
""",
            "input": {
                "message": "prepare to die in this many ways:",
                "start": 5,
                "stop": 2,
                "completion_message": "or not, I guess",
            },
        },
        {
            "expect": """Getting ready to start in 9
Getting ready to start in 8
Getting ready to start in 7
Getting ready to start in 6
Getting ready to start in 5
Getting ready to start in 4
Getting ready to start in 3
Getting ready to start in 2
Getting ready to start in 1
Let's go!
""",
            "input": {
                "message": "Getting ready to start in",
                "start": 9,
                "stop": 1,
                "completion_message": "Let's go!",
            },
        },
    ]
    for countdown in book_of_counts:
        try:
            # https://stackoverflow.com/a/34738440/1835727
            capturedOutput = io.StringIO()  # Create StringIO object
            sys.stdout = capturedOutput  #  and redirect stdout.

            exercise1.countdown(**countdown["input"])  # Call function.

            sys.stdout = sys.__stdout__  # Reset redirect.

            if capturedOutput.getvalue() != countdown["expect"]:
                print("Captured:\n" + capturedOutput.getvalue())  # Now works as before.
                print("Expected:\n" + countdown["expect"])

            testResults.append(
                test(
                    capturedOutput.getvalue() == countdown["expect"],
                    "Exercise 1: countdown!! Output check",
                )
            )
        except Exception as e:
            sys.stdout = sys.__stdout__  # Reset redirect.
            print("countdown test failed", e)
            testResults.append(test(False, "Exercise 1: countdown!! Output check"))

    function_text = inspect.getsource(exercise1.countdown)
    countdown_function_body = "".join(function_text)
    testResults.append(
        test(
            countdown_function_body.count("print") <= 2,
            "Exercise 1: countdown!! rewrite content - fewer print calls",
        )
    )
    if countdown_function_body.count("print") > 2:
        print(function_text)
        print(
            "do you really need all those calls to print?",
            "Could you get by with only 2?",
        )

    triangles = [
        {
            "area": 6.0,
            "aspect": "tall",
            "base": 3,
            "height": 4,
            "hypotenuse": 5.0,
            "perimeter": 12.0,
            "units": "mm",
        },
        {
            "area": 15,
            "aspect": "wide",
            "base": 10,
            "height": 3,
            "hypotenuse": 10.44030650891055,
            "perimeter": 23.440306508910552,
            "units": "mm",
        },
        {
            "area": 60.0,
            "aspect": "tall",
            "base": 8,
            "height": 15,
            "hypotenuse": 17.0,
            "perimeter": 40.0,
            "units": "mm",
        },
        {
            "area": 12.5,
            "aspect": "equal",
            "base": 5,
            "height": 5,
            "hypotenuse": 7.0710678118654755,
            "perimeter": 17.071067811865476,
            "units": "mm",
        },
        {
            "area": 180.0,
            "aspect": "tall",
            "base": 9,
            "height": 40,
            "hypotenuse": 41.0,
            "perimeter": 90.0,
            "units": "mm",
        },
    ]

    pattern = "Exercise {}: {}: {}×{}⇨{}"
    for t in triangles:
        hyp = exercise1.calculate_hypotenuse(t["base"], t["height"])
        testResults.append(
            test(
                hyp == t["hypotenuse"],
                pattern.format(
                    1, "calculate_hypotenuse", t["base"], t["height"], t["hypotenuse"]
                ),
            )
        )
        if hyp != t["hypotenuse"]:
            print(
                f"You said that a b{t['base']}×h{t['height']} "
                f"right triangle has a hyp of ⇨ {hyp}"
            )

        area = exercise1.calculate_area(t["base"], t["height"])
        testResults.append(
            test(
                area == t["area"],
                pattern.format(1, "calculate_area", t["base"], t["height"], t["area"]),
            )
        )
        if area != t["area"]:
            print(
                f"You said that a b{t['base']}×h{t['height']} "
                f"right triangle has n area of ⇨ {area}"
            )

        aspect = exercise1.calculate_aspect(t["base"], t["height"])
        testResults.append(
            test(
                aspect == t["aspect"],
                pattern.format(
                    1, "calculate_aspect", t["base"], t["height"], t["aspect"]
                ),
            )
        )

        perimeter = exercise1.calculate_perimeter(t["base"], t["height"])
        testResults.append(
            test(
                perimeter == t["perimeter"],
                pattern.format(
                    1, "calculate_perimeter", t["base"], t["height"], t["perimeter"]
                ),
            )
        )

        facts = exercise1.get_triangle_facts(t["base"], t["height"])
        testResults.append(
            test(
                facts == t,
                pattern.format(1, "get_triangle_facts", t["base"], t["height"], t),
            )
        )

        facts = exercise1.get_triangle_facts(t["base"], t["height"])
        diagram = exercise1.tell_me_about_this_right_triangle(facts)
        testName = "exercise 1: draw a diagram\n" + str(diagram)
        testResults.append(
            test(test_diagrams(diagram=diagram, expected=facts["aspect"]), testName)
        )

    ff = exercise1.triangle_master(
        base=5, height=5, return_diagram=False, return_dictionary=False
    )
    testResults.append(
        test(
            ff is None, "exercise 1: triangle_master diagram: False, dictionary: False"
        )
    )

    tf = exercise1.triangle_master(
        base=5, height=5, return_diagram=True, return_dictionary=False
    )
    testResults.append(
        test(
            type(tf) is str,
            "exercise 1: triangle_master diagram: True, dictionary: False",
        )
    )

    ft = exercise1.triangle_master(
        base=5, height=5, return_diagram=False, return_dictionary=True
    )
    testResults.append(
        test(
            type(ft) is dict,
            "exercise 1: triangle_master diagram: False, dictionary: True"
            " -- type(ft) is dict",
        )
    )
    try:
        testResults.append(
            test(
                "units" in ft,
                "exercise 1: triangle_master diagram: False, dictionary: True"
                ' -- "units" in ft["facts"]',
            )
        )
    except Exception as e:
        testResults.append(
            test(
                False,
                "exercise 1: triangle_master diagram: False, dictionary: True"
                ' -- "units" in ft["facts"]',
            )
        )

    tt = exercise1.triangle_master(
        base=5, height=5, return_diagram=True, return_dictionary=True
    )
    try:
        testResults.append(
            test(
                type(tt) is dict and type(tt["diagram"]) is str,
                "exercise 1: triangle_master diagram: T, dictionary: T",
            )
        )
    except Exception as e:
        print(e)
        testResults.append(
            test(False, "exercise 1: triangle_master diagram: T, dictionary: T")
        )

    pattern = "Exercise 1: get_triangle_facts uses {}"
    for function_name in [
        "calculate_hypotenuse",
        "calculate_area",
        "calculate_perimeter",
        "calculate_aspect",
    ]:
        testResults.append(
            test(
                function_name in exercise1.get_triangle_facts.__code__.co_names,
                pattern.format(function_name),
            )
        )

    for length in zip([5, 8, 4, 0, "a"], [5, 8, 4, None, None]):
        try:
            word = exercise1.get_a_word_of_length_n(length[0])
            testResults.append(
                test(
                    test_word_length(
                        word=word, requested_length=length[0], expected_length=length[1]
                    ),
                    f"exercise 1: get_a_word_of_length_n {word}",
                )
            )
        except Exception as e:
            print(e)
            testResults.append(
                test(False, f"exercise 1: get_a_word_of_length_n {length}")
            )

    some_lengths = [[4, 5, 6], [4, 18, 4]]
    for lengths in some_lengths:
        try:
            words = exercise1.list_of_words_with_lengths(lengths)
            if words is not None:
                checks = [len(x[0]) == x[1] for x in zip(words, lengths)]
            else:
                checks = [False]
            print(words, lengths, checks)
            testResults.append(
                test(all(checks), "exercise 1: list_of_words_with_lengths {word}",)
            )
        except Exception as e:
            print(e)
            testResults.append(
                test(False, f"exercise 1: list_of_words_with_lengths {lengths}")
            )
    try:
        testResults.append(
            test(
                "list_of_words_with_lengths"
                in exercise1.wordy_pyramid.__code__.co_names,
                "exercise 1: wordy_pyramid has been refactored",
                # write a better error message
            )
        )
    except Exception as e:
        testResults.append(test(False, "exercise 1: wordy_pyramid has been refactored"))

    lengths = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
    works = None
    try:
        words = exercise1.wordy_pyramid()
        expected = [len(w) for w in words]
        works = expected == lengths
        print("expected     ", expected, "\ngiven lengths", lengths)
        [print(w + " " + str(len(w))) for w in words]
    except Exception as e:
        works = False
        print("Exercise 1: wordy_pyramid is broken", e)
    testResults.append(test(works, "Exercise 1: wordy_pyramid still works"))

    # EXERCISE 2 tests
    path = f"{path_to_code_to_check}/week{WEEK_NUMBER}/exercise2.py"
    print(path)

    e2 = loadExerciseFile(
        path_to_code_to_check, weekNumber=WEEK_NUMBER, exerciseNumber=2
    )

    # Linter test
    # print("Linter test:", path)
    # testResults.append(
    #     test(test_flake8(path),
    #          "Exercise 2: pass the linter"))

    # pydocstyle test
    # print("Docstyle test:", path)
    # testResults.append(
    #     test(test_pydocstyle(path),
    #          "Exercise 2: pass the pydocstyle test"))

    source = ["baaab", "b", "roof", "hell"]
    result = [
        "bbaoaaobaobaobbbaaobaobbbaaobaobbbabbaoaaob",
        "bbaoaaob",
        "roabbaoabbaf",
        "hell",
    ]
    for source, result in zip(source, result):
        try:
            testResults.append(
                test(
                    e2.abba(source, 2) == result, f"exercise 2: abba {source}⇨{result}"
                )
            )
        except Exception as e:
            testResults.append(test(False, f"exercise 2: abba {source}⇨{result}"))

    testResults.append(
        test(
            e2.draw_square(2) == "2100000100000100000100000100000",
            "exercise 2: Koch _|-|_",
        )
    )
    testResults.append(
        test(e2.draw_pointy(2) == "210000100001000010000", "exercise 2: Koch _^_")
    )

    # CLEANUP AND FINISH

    message = "Rad, you've got all the tests passing!"

    return finish_up(testResults, message, nyan_cat())


if __name__ == "__main__":
    theTests()
