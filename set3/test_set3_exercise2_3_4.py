# -*- coding: UTF-8 -*-
"""Tests for Set 3, Exercises 2-4 - Guessing Games and Binary Search.

Complete implementation matching original tests with all scenarios.
"""

import math
import os
import pytest
import random
from unittest import mock
from colorama import Fore

EM = Fore.YELLOW
NORM = Fore.WHITE
TIMEOUT = 3


@pytest.fixture
def exercise2(load_exercise):
    """Load exercise 2 module."""
    return load_exercise(set_number=3, exercise_number=2)


@pytest.fixture
def exercise3(load_exercise):
    """Load exercise 3 module."""
    return load_exercise(set_number=3, exercise_number=3)


@pytest.fixture
def exercise4(load_exercise):
    """Load exercise 4 module."""
    return load_exercise(set_number=3, exercise_number=4)


@pytest.mark.set3
@pytest.mark.exercise2
@pytest.mark.mock_input
@pytest.mark.timeout(TIMEOUT)
def test_example_guessing_game(exercise2):
    """Test the example guessing game (provided code)."""
    upper_bound = 5
    guesses = list(range(5 + 1))
    mock_inputs = [upper_bound] + guesses
    
    with mock.patch('builtins.input', side_effect=mock_inputs):
        result = exercise2.exampleGuessingGame()
        assert result == "You got it!", f"Expected 'You got it!', got {result}"


@pytest.mark.set3
@pytest.mark.exercise3
@pytest.mark.mock_input
@pytest.mark.timeout(TIMEOUT)
class TestAdvancedGuessingGame:
    """Test the advanced guessing game with various scenarios.
    
    These tests match the original test suite's comprehensive scenarios.
    """
    
    def test_guessing_game_basic(self, exercise3):
        """Test guessing game with basic upper and lower bounds."""
        lower_bound = 10
        upper_bound = 15
        guesses = list(range(lower_bound, upper_bound + 1))
        mock_inputs = [lower_bound, upper_bound] + guesses
        
        with mock.patch('builtins.input', side_effect=mock_inputs):
            result = exercise3.advancedGuessingGame()
            assert result == "You got it!", (
                f"Expected 'You got it!', got {result}\n"
                f"Inputs: lower={lower_bound}, upper={upper_bound}, then guesses"
            )
    
    def test_guessing_game_polite_failures(self, exercise3):
        """Test game handles non-numeric inputs gracefully."""
        lower_bound = 10
        upper_bound = 15
        guesses = list(range(lower_bound, upper_bound + 1))
        # Start with invalid inputs ("ten", "cats") before valid ones
        mock_inputs = ["ten", lower_bound, upper_bound, "cats"] + guesses
        
        with mock.patch('builtins.input', side_effect=mock_inputs):
            result = exercise3.advancedGuessingGame()
            assert result == "You got it!", (
                "Game should handle non-numeric inputs gracefully and continue"
            )
    
    def test_guessing_game_lower_bigger_than_upper(self, exercise3):
        """Test game when user enters lowerBound > upperBound."""
        lower_bound = 10
        upper_bound = 15
        second_guess = 25  # This will be entered as upper bound, but it's > first
        guesses = list(range(lower_bound, second_guess + 1))
        mock_inputs = [lower_bound, upper_bound, second_guess] + guesses
        
        with mock.patch('builtins.input', side_effect=mock_inputs):
            result = exercise3.advancedGuessingGame()
            assert result == "You got it!", (
                "Game should handle case where bounds are entered incorrectly"
            )
    
    def test_guessing_game_no_range_delta_1(self, exercise3):
        """Test game with no range to guess in (upperBound - lowerBound = 1)."""
        lower_bound = 10
        upper_bound = 11  # Only 1 number difference
        second_guess = 15
        guesses = list(range(lower_bound, second_guess + 1))
        mock_inputs = [lower_bound, upper_bound, second_guess] + guesses
        
        with mock.patch('builtins.input', side_effect=mock_inputs):
            result = exercise3.advancedGuessingGame()
            assert result == "You got it!", (
                "Game should handle edge case where range is just 1 number"
            )
    
    def test_guessing_game_no_range_equal(self, exercise3):
        """Test game with no range (upperBound == lowerBound)."""
        lower_bound = 10
        upper_bound = 10  # Same number!
        second_guess = 15
        guesses = list(range(lower_bound, second_guess + 1))
        mock_inputs = [lower_bound, upper_bound, second_guess] + guesses
        
        with mock.patch('builtins.input', side_effect=mock_inputs):
            result = exercise3.advancedGuessingGame()
            assert result == "You got it!", (
                "Game should handle edge case where upper and lower are equal"
            )


@pytest.mark.set3
@pytest.mark.exercise4
@pytest.mark.timeout(TIMEOUT)
class TestBinarySearch:
    """Test binary search implementation and efficiency.
    
    Binary search should complete in O(log n) time.
    """
    
    def test_binary_search_1_100_5(self, exercise4):
        """Test binary search (1, 100, 5) - looking low."""
        result = exercise4.binary_search(1, 100, 5)
        
        assert "guess" in result, "Result should contain 'guess' key"
        assert "tries" in result, "Result should contain 'tries' key"
        
        worst_case = math.log(99, 2)  # log base 2 of range
        
        if result["tries"] == 0 and result["guess"] == 0:
            pytest.fail(
                f"\n{EM}guess and tries are both 0{NORM}\n"
                "You probably haven't started yet, or you're not updating "
                "them as you try different options."
            )
        elif result["tries"] == 0:
            pytest.fail(
                f"\n{EM}tries is 0{NORM}\n"
                "That probably means you haven't started yet."
            )
        
        assert result["guess"] == 5, f"Should find 5, got {result['guess']}"
        
        if result["tries"] < worst_case:
            print(f"🎯 Snuck it in! {result['tries']} tries (worst case: {worst_case:.1f})")
        elif result["tries"] < worst_case + 1:
            print(f"✅ One over worst case, but that's ok! {result['tries']} tries")
        else:
            pytest.fail(
                f"\n{EM}Binary search too slow!{NORM}\n"
                f"Took {result['tries']} tries, should get it in under {worst_case:.1f} tries.\n"
                f"Binary search should complete in O(log n) time."
            )
    
    def test_binary_search_1_100_6(self, exercise4):
        """Test binary search (1, 100, 6) - looking low."""
        result = exercise4.binary_search(1, 100, 6)
        worst_case = math.log(99, 2)
        
        assert result["guess"] == 6, f"Should find 6, got {result['guess']}"
        assert result["tries"] <= worst_case + 1, (
            f"Should complete in ~{worst_case:.1f} tries, took {result['tries']}"
        )
    
    def test_binary_search_1_100_95(self, exercise4):
        """Test binary search (1, 100, 95) - looking high."""
        result = exercise4.binary_search(1, 100, 95)
        worst_case = math.log(99, 2)
        
        assert result["guess"] == 95, f"Should find 95, got {result['guess']}"
        assert result["tries"] <= worst_case + 1, (
            f"Should complete in ~{worst_case:.1f} tries, took {result['tries']}"
        )
    
    def test_binary_search_1_51_5(self, exercise4):
        """Test binary search (1, 51, 5) - smaller range."""
        result = exercise4.binary_search(1, 51, 5)
        worst_case = math.log(50, 2)
        
        assert result["guess"] == 5, f"Should find 5, got {result['guess']}"
        assert result["tries"] <= worst_case + 1, (
            f"Should complete in ~{worst_case:.1f} tries, took {result['tries']}"
        )
    
    def test_binary_search_1_50_5(self, exercise4):
        """Test binary search (1, 50, 5) - power of 2 range."""
        result = exercise4.binary_search(1, 50, 5)
        worst_case = math.log(49, 2)
        
        assert result["guess"] == 5, f"Should find 5, got {result['guess']}"
        assert result["tries"] <= worst_case + 1, (
            f"Should complete in ~{worst_case:.1f} tries, took {result['tries']}"
        )
    
    @pytest.mark.parametrize("iteration", range(10))
    def test_binary_search_random_values(self, exercise4, iteration):
        """Test binary search with randomly generated test values.
        
        This runs 10 times with random parameters to catch edge cases.
        """
        low = 0
        high = 100
        target = random.randint(low + 1, high - 1)
        
        result = exercise4.binary_search(low, high, target)
        worst_case = math.log(high - low, 2)
        
        assert result["guess"] == target, (
            f"Should find {target}, got {result['guess']}"
        )
        assert result["tries"] <= worst_case + 1, (
            f"Random test #{iteration}: search({low}, {high}, {target}) "
            f"should complete in ~{worst_case:.1f} tries, took {result['tries']}"
        )


@pytest.mark.set3
@pytest.mark.exercise4
@pytest.mark.slow
def test_binary_search_visualization(exercise4):
    """Optional: Visualize binary search performance over many iterations.
    
    This test creates a histogram showing the efficiency of the binary search
    implementation over 1000 random test cases. It's marked as 'slow' so it
    can be skipped during normal test runs.
    
    Only shows visualization if binary search is working correctly.
    """
    # First check if basic binary search works
    basic_test = exercise4.binary_search(1, 10, 5)
    if basic_test.get("tries", 0) == 0:
        pytest.skip("Binary search not implemented yet")
    
    # Only run visualization for students (not for marking)
    if os.environ.get("USERNAME") == "bdoherty":
        pytest.skip("Skipping visualization during marking")
    
    try:
        import matplotlib.pyplot as plt
        
        BASE2 = 2
        results = []
        test_runs = 1000
        
        for _ in range(test_runs):
            low = random.randint(-100, 100)
            high = random.randint(low + 2, 200)
            target = random.randint(low + 1, high - 1)
            
            bs = exercise4.binary_search(low, high, target)
            tries = bs["tries"]
            worst = math.log(high - low, BASE2)
            ratio = tries / worst
            results.append(ratio)
        
        plt.hist(results, bins=20)
        plt.title(f"Binary Search Performance Over {test_runs} Iterations")
        plt.xlabel("Proportion of Worst Case (O(log n))")
        plt.ylabel("Frequency")
        
        print(
            "\n📊 Binary Search Performance Histogram\n"
            "=" * 60 + "\n"
            "This shows how many guesses your search took relative to worst case.\n"
            "The worst case is the base-2 log of the range.\n"
            "E.g., range of 16 → worst case is 4 guesses (2^4 = 16)\n\n"
            "Your implementation should always be at or below 1.0 on the x-axis,\n"
            "meaning you're as good as or better than the theoretical worst case.\n\n"
            "Close the histogram window to continue testing.\n"
            "=" * 60
        )
        plt.show()
        
    except ImportError:
        print(
            "\n" + "🍌" * 30 + "\n"
            "You don't have matplotlib installed yet.\n"
            "It's a library for making graphs and charts - we'll use it soon!\n"
            "To install it, run:\n\n"
            "    pip install matplotlib\n\n"
            + "🍌" * 30
        )
