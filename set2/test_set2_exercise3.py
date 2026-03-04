# -*- coding: UTF-8 -*-
"""Tests for Set 2, Exercise 3.

Tests loops, conditionals, and complex data structures.
This exercise has many helpful error messages for common student mistakes.
"""

import pytest
from colorama import Fore

EM = Fore.YELLOW
NORM = Fore.WHITE


@pytest.fixture
def exercise3(load_exercise):
    """Load exercise 3 module."""
    return load_exercise(set_number=2, exercise_number=3)


@pytest.mark.exercise3
@pytest.mark.set2
class TestConditionals:
    """Test basic conditional logic."""
    
    def test_is_odd_even(self, exercise3):
        """Test is_odd with an even number."""
        assert exercise3.is_odd(2) is False, "2 should not be odd"
    
    def test_is_odd_odd(self, exercise3):
        """Test is_odd with an odd number."""
        assert exercise3.is_odd(5) is True, "5 should be odd"
    
    @pytest.mark.parametrize("moves,should_move,expected", [
        (True, True, "No Problem"),
        (True, False, "Duct Tape"),
        (False, True, "WD-40"),
        (False, False, "No Problem"),
    ])
    def test_fix_it(self, exercise3, moves, should_move, expected):
        """Test fix_it function with all scenarios."""
        result = exercise3.fix_it(moves, should_move)
        
        it = "moves" if moves else "does not move"
        should = "" if should_move else "not"
        
        assert result == expected, (
            f"When it {it} and it should {should} move, "
            f"expected '{expected}' but got '{result}'"
        )


@pytest.mark.exercise3
@pytest.mark.set2
class TestBasicLoops:
    """Test basic loop construction."""
    
    def test_loops_1a(self, exercise3):
        """Test loops_1a - basic 1D list of 10 stars."""
        result = exercise3.loops_1a()
        expected = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        
        # Check for None return (common mistake)
        if result is None:
            pytest.fail(
                f"\n{EM}You returned None!{NORM}\n"
                f"Common causes:\n"
                f"  • Did you forget to {EM}return{NORM} the result?\n"
                f"  • Are you using {EM}return print(something){NORM}? That returns None!\n"
                f"  • Remember: {EM}print{NORM} displays output but returns None\n"
                f"\n{EM}Fix:{NORM} You need to return the computed value, not print it.\n"
                f"Either assign the list to a variable and return it, or return it directly."
            )
        
        # Check for string instead of list (another common mistake)
        if result == "**********":
            pytest.fail(
                f"\n{EM}You returned a string, but we need a list!{NORM}\n"
                f"Expected: {EM}{expected}{NORM}\n"
                f"Got: {EM}{result}{NORM}\n"
                f"\nHint: Use square brackets [] to make a list, not quotes \"\"."
            )
        
        assert result == expected, (
            f"Expected a list of 10 stars: {expected}\n"
            f"Got: {result}"
        )
    
    def test_loops_1c(self, exercise3):
        """Test loops_1c - 1D list with arguments."""
        result = exercise3.loops_1c(3, ":)")
        expected = [":)", ":)", ":)"]
        
        assert result == expected, (
            f"loops_1c(3, ':)') should return [':)', ':)', ':)']\n"
            f"Got: {result}"
        )


@pytest.mark.exercise3
@pytest.mark.set2
class Test2DLoops:
    """Test 2D list construction."""
    
    def test_loops_2(self, exercise3):
        """Test loops_2 - 10x10 grid of stars."""
        result = exercise3.loops_2()
        expected = [
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
        
        assert result == expected, "Expected a 10x10 grid of stars"
    
    def test_loops_3(self, exercise3):
        """Test loops_3 - 10 lists where each contains 10 matching numbers."""
        result = exercise3.loops_3()
        expected = [
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
        
        assert result == expected, "Each row should contain 10 matching numbers (as strings)"
    
    def test_loops_4(self, exercise3):
        """Test loops_4 - 10 rising lists."""
        result = exercise3.loops_4()
        expected = [
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
        
        if result is None:
            pytest.fail(
                f"\n{EM}Still returning None!{NORM}\n"
                f"Did you forget the return statement?"
            )
        
        # Check if they're using numbers instead of strings
        if result and len(result) == 10 and len(result[0]) == 10:
            if isinstance(result[0][0], int):
                pytest.fail(
                    f"\n{EM}Close, but not quite!{NORM}\n"
                    f"The test is looking for {EM}strings{NORM}, not numbers.\n"
                    f"You have: {result[0]} (numbers)\n"
                    f"We want: {expected[0]} (strings)\n"
                    f"\nHint: Look into what the {EM}str(){NORM} function does!"
                )
        
        assert result == expected, (
            f"Expected 10 rising lists of string digits.\n"
            f"Got: {result}"
        )
    
    def test_loops_5(self, exercise3):
        """Test loops_5 - coordinate grid."""
        result = exercise3.loops_5()
        expected = [
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
        
        assert result == expected, "Expected coordinate strings like (i0, j0)"


@pytest.mark.exercise3
@pytest.mark.set2
class TestAdvancedLoops:
    """Test more advanced loop patterns."""
    
    def test_loops_6(self, exercise3):
        """Test loops_6 - wedge pattern."""
        result = exercise3.loops_6()
        expected = [
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
        
        assert result == expected, (
            "Expected a wedge pattern where each row gets progressively longer"
        )
    
    def test_loops_7(self, exercise3):
        """Test loops_7 - pyramid of stars."""
        result = exercise3.loops_7()
        expected = [
            [" ", " ", " ", " ", "*", " ", " ", " ", " "],
            [" ", " ", " ", "*", "*", "*", " ", " ", " "],
            [" ", " ", "*", "*", "*", "*", "*", " ", " "],
            [" ", "*", "*", "*", "*", "*", "*", "*", " "],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ]
        
        assert result == expected, (
            "Expected a pyramid pattern with stars centered and expanding"
        )
