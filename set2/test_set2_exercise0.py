# -*- coding: UTF-8 -*-
"""Tests for Set 2, Exercise 0.

Tests basic function writing: addition and string manipulation.
"""

import inspect
import pytest
import ast
from colorama import Fore
from conftest import check_print_instead_of_return


EM = Fore.YELLOW
NORM = Fore.WHITE


@pytest.fixture
def exercise0(load_exercise):
    """Load exercise 0 module."""
    return load_exercise(set_number=2, exercise_number=0)


@pytest.mark.exercise0
@pytest.mark.set2
class TestAddition:
    """Test addition functions."""

    def test_add_1_positive(self, exercise0):
        """Test add_1 with positive number."""
        assert exercise0.add_1(55) == 56, "55 + 1 should equal 56"

    def test_add_1_negative(self, exercise0):
        """Test add_1 with negative number."""
        assert exercise0.add_1(-5) == -4, "-5 + 1 should equal -4"

    def test_add_1_decimal(self, exercise0):
        """Test add_1 with decimal number."""
        result = exercise0.add_1(0.1)
        assert abs(result - 1.1) < 0.001, "0.1 + 1 should equal 1.1"

    def test_add_5_positive(self, exercise0):
        """Test add_5 with positive number."""
        assert exercise0.add_5(55) == 60, "55 + 5 should equal 60"

    def test_add_5_negative(self, exercise0):
        """Test add_5 with negative number."""
        assert exercise0.add_5(-5) == 0, "-5 + 5 should equal 0"

    def test_add_5_decimal(self, exercise0):
        """Test add_5 with decimal number."""
        result = exercise0.add_5(0.1)
        assert abs(result - 5.1) < 0.001, "0.1 + 5 should equal 5.1"

    def test_adder_positive(self, exercise0):
        """Test adder with positive numbers."""
        assert exercise0.adder(5, 5) == 10, "5 + 5 should equal 10"

    def test_adder_negative(self, exercise0):
        """Test adder with negative numbers."""
        assert exercise0.adder(-5, -5) == -10, "-5 + -5 should equal -10"

    def test_adder_decimal(self, exercise0):
        """Test adder with decimal numbers."""
        result = exercise0.adder(0.1, 0.9)
        assert abs(result - 1.0) < 0.001, "0.1 + 0.9 should equal 1"


@pytest.mark.exercise0
@pytest.mark.set2
class TestStringManipulation:
    """Test string manipulation functions."""

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("you've", "YOU'VE"),
            ("got", "GOT"),
            ("to", "TO"),
            ("fight", "FIGHT"),
            ("for", "FOR"),
            ("your", "YOUR"),
            ("right", "RIGHT"),
            ("to", "TO"),
            ("party", "PARTY"),
        ],
    )
    def test_shout(self, exercise0, word, expected):
        """Test shout function with various words."""
        assert (
            exercise0.shout(word) == expected
        ), f"shout('{word}') should return '{expected}'"

    def test_really_shout(self, exercise0):
        """Test really_shout function returns correct result."""
        assert (
            exercise0.really_shout("hello") == "HELLO!"
        ), "really_shout('hello') should return 'HELLO!'"

    def test_really_shout_empty(self, exercise0):
        """Test really_shout with empty string."""
        assert exercise0.really_shout("") == "!", "really_shout('') should return '!'"

    def test_really_shout_with_exclamation(self, exercise0):
        """Test really_shout when string already has exclamation."""
        assert (
            exercise0.really_shout("wow!") == "WOW!!"
        ), "really_shout('wow!') should return 'WOW!!'"

    def test_really_shout_refactoring(self, exercise0):
        """Test that really_shout REUSES the shout() function (DRY principle).

        This is an important lesson: Don't Repeat Yourself (DRY).
        The exercise explicitly asks students to reuse shout() rather than
        duplicating the .upper() logic.
        """

        source = inspect.getsource(exercise0.really_shout)

        # Parse the source to find actual function calls
        tree = ast.parse(source)

        # Find all function calls in the body
        calls = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    calls.append(node.func.id)

        # Check if they're calling shout()
        if "shout" not in calls:
            pytest.fail(
                f"\n{EM}Your really_shout() function should call shout()!{NORM}\n"
                f"\n"
                f"  The exercise asks you to reuse the shout() function.\n"
                f"  This is the DRY principle: Don't Repeat Yourself.\n"
                f"\n"
                f"  {EM}Instead of duplicating logic like this:{NORM}\n"
                f"    def really_shout(text):\n"
                f"        return text.upper() + '!'  {EM}← Duplicates .upper() logic{NORM}\n"
                f"\n"
                f"  {EM}Reuse the existing shout() function:{NORM}\n"
                f"    def really_shout(text):\n"
                f"        return shout(text) + '!'  {EM}← Much better!{NORM}\n"
                f"\n"
                f"  Why? If you later need to change how shouting works,\n"
                f"  you only need to update one place!\n"
            )

    def test_really_shout_not_printing(self, exercise0, capsys):
        """Test that really_shout returns rather than prints."""
        result, error_msg = check_print_instead_of_return(
            exercise0.really_shout, ("test",), "TEST!", capsys
        )
        if error_msg:
            pytest.fail(error_msg)
        assert result == "TEST!", "really_shout('test') should return 'TEST!'"

    def test_shout_with_a_number(self, exercise0):
        """Test shout_with_a_number function."""
        result = exercise0.shout_with_a_number("hi", 1)
        assert result == "HI 1", "shout_with_a_number('hi', 1) should return 'HI 1'"
