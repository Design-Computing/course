# -*- coding: UTF-8 -*-
"""Tests for Set 4, Exercise 1 - File I/O and API Requests.

Tests JSON file reading, API requests, and file writing.
"""

import json
import os
import pytest
from colorama import Fore

EM = Fore.YELLOW
NORM = Fore.WHITE


@pytest.fixture
def exercise1(load_exercise):
    """Load exercise 1 module."""
    return load_exercise(set_number=4, exercise_number=1)


@pytest.mark.set4
@pytest.mark.exercise1
def test_get_some_details(exercise1):
    """Test getting specific data from lazyduck.json."""
    expected = {
        "lastName": "hoogmoed",
        "password": "jokers",
        "postcodePlusID": 4311240
    }
    
    try:
        result = exercise1.get_some_details()
        assert result == expected, (
            f"Expected to extract specific fields from lazyduck.json\n"
            f"Expected: {expected}\n"
            f"Got: {result}"
        )
    except Exception as e:
        pytest.fail(
            f"\n{EM}Error reading JSON file!{NORM}\n"
            f"Make sure you're reading lazyduck.json and extracting:\n"
            f"  • lastName\n"
            f"  • password\n"
            f"  • postcodePlusID (calculated from postcode + ID)\n"
            f"\nError: {e}"
        )


@pytest.mark.set4
@pytest.mark.exercise1
@pytest.mark.api_call
def test_wordy_pyramid(exercise1):
    """Test requesting words from an API and building a pyramid."""
    expected_lengths = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
    
    try:
        pyramid = exercise1.wordy_pyramid()
        
        if pyramid is None:
            pytest.fail(
                f"\n{EM}wordy_pyramid returned None!{NORM}\n"
                "Did you forget to return the result?\n"
                "The function should request words from an API and return a list."
            )
        
        p_lengths = [len(w) for w in pyramid]
        
        assert p_lengths == expected_lengths, (
            f"\n{EM}Word lengths don't match!{NORM}\n"
            f"Expected lengths: {expected_lengths}\n"
            f"Got lengths: {p_lengths}\n"
            f"Your pyramid: {pyramid}\n\n"
            "The pyramid should grow from 3 to 20 letters in steps of 2,\n"
            "then shrink back down: [3, 5, 7, ..., 19, 20, 18, ..., 6, 4]"
        )
        
    except Exception as e:
        pytest.fail(
            f"\n{EM}Error in wordy_pyramid!{NORM}\n"
            f"Error: {e}\n"
            "Make sure you're:\n"
            "  1. Making API requests to get words\n"
            "  2. Building a pyramid pattern with the word lengths\n"
            "  3. Returning the list of words"
        )


@pytest.mark.set4
@pytest.mark.exercise1
def test_lasers_pew_file_exists(repo_path):
    """Test that lasers.pew file was created."""
    file_path = os.path.join(repo_path, "set4", "lasers.pew")
    
    assert os.path.isfile(file_path), (
        f"\n{EM}lasers.pew file not found!{NORM}\n"
        f"Expected location: {file_path}\n"
        "You need to create this file with exactly the number 6 in it."
    )


@pytest.mark.set4
@pytest.mark.exercise1
def test_lasers_pew_content(repo_path):
    """Test that lasers.pew contains the correct number."""
    file_path = os.path.join(repo_path, "set4", "lasers.pew")
    
    if not os.path.isfile(file_path):
        pytest.skip("lasers.pew file doesn't exist yet")
    
    with open(file_path, "r") as f:
        content = f.read().strip()
    
    try:
        count = int(content)
        assert count == 6, (
            f"\n{EM}lasers.pew should contain the number 6!{NORM}\n"
            f"Currently contains: {content}\n"
            "This is testing your ability to write to a file."
        )
    except ValueError:
        pytest.fail(
            f"\n{EM}lasers.pew should contain a number!{NORM}\n"
            f"Currently contains: {content}\n"
            "It should contain only the number 6."
        )
