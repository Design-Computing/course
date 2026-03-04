# -*- coding: UTF-8 -*-
"""Tests for Set 3, Exercise 1 - Loops and User Input.

Tests loop_ranger, two_step_ranger, stubborn_asker, not_number_rejector, and super_asker.
These mirror the original test structure with full timeout and mock input handling.
"""

import pytest
from unittest import mock
from colorama import Fore

EM = Fore.YELLOW
NORM = Fore.WHITE
TIMEOUT = 3  # seconds


@pytest.fixture
def exercise1(load_exercise):
    """Load exercise 1 module."""
    return load_exercise(set_number=3, exercise_number=1)


@pytest.mark.set3
@pytest.mark.exercise1
class TestLoopRanger:
    """Test loop_ranger function."""
    
    def test_loop_ranger_3_8_1(self, exercise1):
        """Test loop_ranger(3, 8, 1) == [3, 4, 5, 6, 7]."""
        result = exercise1.loop_ranger(3, 8, 1)
        expected = [3, 4, 5, 6, 7]
        assert result == expected, f"loop_ranger(3, 8, 1) should return {expected}, got {result}"
    
    def test_loop_ranger_100_104_2(self, exercise1):
        """Test loop_ranger(100, 104, 2) == [100, 102]."""
        result = exercise1.loop_ranger(100, 104, 2)
        expected = [100, 102]
        assert result == expected, f"loop_ranger(100, 104, 2) should return {expected}, got {result}"


@pytest.mark.set3
@pytest.mark.exercise1
class TestTwoStepRanger:
    """Test two_step_ranger function."""
    
    def test_two_step_ranger_0_10(self, exercise1):
        """Test two_step_ranger(0, 10) == [0, 2, 4, 6, 8]."""
        result = exercise1.two_step_ranger(0, 10)
        expected = [0, 2, 4, 6, 8]
        assert result == expected, f"two_step_ranger(0, 10) should return {expected}, got {result}"
    
    def test_two_step_ranger_100_104(self, exercise1):
        """Test two_step_ranger(100, 104) == [100, 102]."""
        result = exercise1.two_step_ranger(100, 104)
        expected = [100, 102]
        assert result == expected, f"two_step_ranger(100, 104) should return {expected}, got {result}"


@pytest.mark.set3
@pytest.mark.exercise1
@pytest.mark.mock_input
@pytest.mark.timeout(TIMEOUT)
class TestStubbornAsker:
    """Test stubborn_asker function with mocked inputs."""
    
    def test_stubborn_asker_10_20(self, exercise1):
        """Test stubborn_asker keeps asking until valid input in range."""
        # Values from low-25 to high+20, stepping by 5
        # For low=10, high=20: starts at -15, goes to 40
        # First value in range [10, 20] would be 10
        mock_inputs = list(range(10 - 25, 20 + 20, 5))
        
        with mock.patch("builtins.input", side_effect=mock_inputs):
            result = exercise1.stubborn_asker(10, 20)
            
            if result is None:
                pytest.fail(
                    f"\n{EM}stubborn_asker returned None!{NORM}\n"
                    "Maybe you haven't started yet?\n"
                    "The function should keep asking for input until "
                    "it gets a number between low and high."
                )
            
            assert 10 <= result <= 20, (
                f"stubborn_asker(10, 20) should return a value between 10 and 20.\n"
                f"Got: {result}"
            )
    
    def test_stubborn_asker_50_60(self, exercise1):
        """Test stubborn_asker with different range."""
        mock_inputs = list(range(50 - 25, 60 + 20, 5))
        
        with mock.patch("builtins.input", side_effect=mock_inputs):
            result = exercise1.stubborn_asker(50, 60)
            assert 50 <= result <= 60, f"Expected value in [50, 60], got {result}"


@pytest.mark.set3
@pytest.mark.exercise1
@pytest.mark.mock_input  
@pytest.mark.timeout(TIMEOUT)
def test_not_number_rejector(exercise1):
    """Test not_number_rejector keeps asking until it gets a number."""
    # First two inputs are not numbers, third is
    mock_inputs = ["a_word", 40, 3.5]
    
    with mock.patch("builtins.input", side_effect=mock_inputs):
        result = exercise1.not_number_rejector("Testing some values:")
        
        # It should return int 40 (or possibly convert to int)
        # The function rejects non-numbers and accepts the first valid number
        assert result is not None, "not_number_rejector should return a value"
        assert isinstance(result, (int, float)), (
            f"Expected a number, got {type(result).__name__}: {result}"
        )


@pytest.mark.set3
@pytest.mark.exercise1
@pytest.mark.mock_input
@pytest.mark.timeout(TIMEOUT)
def test_super_asker(exercise1):
    """Test super_asker combines stubborn_asker and not_number_rejector."""
    # Mix of invalid (non-numbers), out-of-range, and valid numbers
    # Need to provide enough inputs to handle rejection of invalid types AND out of range
    mock_inputs = ["aword", 3.5] + list(range(50 - 25, 60 + 20, 5))
    
    with mock.patch("builtins.input", side_effect=mock_inputs):
        result = exercise1.super_asker(50, 60)
        
        assert result is not None, "super_asker should return a value"
        assert 50 <= result <= 60, (
            f"super_asker(50, 60) should return a value between 50 and 60.\n"
            f"Got: {result}"
        )
