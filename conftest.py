# -*- coding: UTF-8 -*-
"""Root conftest.py for shared pytest fixtures and configuration.

This file provides fixtures and helpers used across all test sets.
"""

import importlib.util as importUtils
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

import pytest
from colorama import Fore, Style, init as colorama_init

# Initialize colorama for cross-platform colored output
colorama_init()

# Add parent directory to path for imports
sys.path.append(os.path.dirname(__file__))

# Import treats for celebration messages
from treats import deadpool, grumpy, nyan_cat, pikachu, pokeball, squirtle

# Colors for output
EM = Fore.YELLOW
NORM = Fore.WHITE


# ============================================================================
# Fixtures for loading student exercise files
# ============================================================================


@pytest.fixture
def repo_path():
    """Return the path to the student's 'me' repository."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "me"))


@pytest.fixture
def load_exercise():
    """Fixture that returns a function to load exercise modules dynamically.

    Usage:
        def test_something(load_exercise):
            exercise1 = load_exercise(set_number=2, exercise_number=1)
            result = exercise1.some_function()
    """

    def _load_exercise(set_number: int, exercise_number: int, path: str = None):
        """Load an exercise file as a module.

        Args:
            set_number: The set number (1, 2, 3, etc.)
            exercise_number: The exercise number (0, 1, 2, etc.)
            path: Optional custom path to the repo (defaults to ../me)

        Returns:
            The loaded module
        """
        if path is None:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "me"))

        exercise_path = os.path.join(
            path, f"set{set_number}", f"exercise{exercise_number}.py"
        )

        spec = importUtils.spec_from_file_location(
            f"exercise{exercise_number}", exercise_path
        )
        module = importUtils.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    return _load_exercise


@pytest.fixture
def check_exercise_runs(repo_path):
    """Fixture to check if an exercise file runs without syntax errors.

    Usage:
        def test_something(check_exercise_runs):
            if check_exercise_runs(set_number=2, exercise_number=1):
                # exercise runs, proceed with tests
    """

    def _check_runs(set_number: int, exercise_number: int) -> bool:
        """Check that an exercise file runs without errors."""
        try:
            exercise_path = os.path.join(
                repo_path, f"set{set_number}", f"exercise{exercise_number}.py"
            )
            spec = importUtils.spec_from_file_location(
                "exercise", os.path.abspath(exercise_path)
            )
            module = importUtils.module_from_spec(spec)
            spec.loader.exec_module(module)
            return True
        except Exception:
            return False

    return _check_runs


# ============================================================================
# Fixtures for common test scenarios
# ============================================================================


@pytest.fixture
def lab_book_completed(repo_path):
    """Check if a lab book (readme.md) has been filled out.

    Usage:
        def test_lab_book(lab_book_completed):
            assert lab_book_completed(set_number=2)
    """

    def _check_lab_book(set_number: int) -> bool:
        """Check if the lab book has actual content."""
        lab_book = Path(os.path.join(repo_path, f"set{set_number}/readme.md"))
        if lab_book.is_file():
            with open(lab_book, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                basic_content = [
                    "TODO: Reflect on what you learned this week and what is still unclear."
                ]
                lines_stripped = [line.strip() for line in lines if line.strip() != ""]

                # If it's just the template, return False
                if lines_stripped == basic_content:
                    return False
                # If there's any content, return True
                elif lines:
                    return True
        return False

    return _check_lab_book


# ============================================================================
# Custom assertion helpers
# ============================================================================


def check_return_none_message(result, context: str = "") -> str:
    """Generate helpful message when student returns None.

    This is a common mistake where students print instead of return.
    """
    if result is None:
        message = (
            f"\n{EM}You returned None!{NORM}\n"
            f"Common causes:\n"
            f"  • Did you forget to {EM}return{NORM} the result?\n"
            f"  • Are you using {EM}return print(something){NORM}? "
            f"That returns None!\n"
            f"  • Did you assign the value but forget to return it?\n"
            f"\n{EM}Remember:{NORM} You need to return the computed value, "
            f"not print it.\n"
        )
        if context:
            message = f"\n{context}\n" + message
        return message
    return ""


def check_print_instead_of_return(func, args, expected_value, capsys):
    """Check if a function printed the expected value instead of returning it.

    This is a VERY common student mistake: they print() the result but forget to return it.
    This helper detects this pattern and provides a helpful error message.

    Args:
        func: The function to test
        args: Arguments to pass (single value or tuple)
        expected_value: The value we expect to be returned
        capsys: The pytest capsys fixture for capturing stdout

    Returns:
        Tuple of (result, helpful_message)
        - result is what the function actually returned
        - helpful_message is None if OK, or a string explaining the mistake

    Example usage in a test:
        def test_add_5(exercise0, capsys):
            result, error_msg = check_print_instead_of_return(
                exercise0.add_5, (55,), 60, capsys
            )
            if error_msg:
                pytest.fail(error_msg)
            assert result == 60, "55 + 5 should equal 60"
    """
    # Call the function and capture any output
    if isinstance(args, tuple):
        result = func(*args)
    else:
        result = func(args)

    captured = capsys.readouterr()

    # Check if they printed the expected value but returned None
    if result is None and captured.out:
        # Check if the expected value appears in output
        if str(expected_value) in captured.out.strip():
            message = (
                f"\n{EM}⚠ It looks like you printed the result instead of returning it!{NORM}\n"
                f"\n"
                f"  Your function returned: {EM}None{NORM}\n"
                f"  But we found this in your output: {EM}{captured.out.strip()}{NORM}\n"
                f"\n"
                f"  {EM}Common mistake:{NORM}\n"
                f"    def my_function(x):\n"
                f"        answer = x + 5\n"
                f"        print(answer)  {EM}← This is wrong!{NORM}\n"
                f"\n"
                f"  {EM}Correct version:{NORM}\n"
                f"    def my_function(x):\n"
                f"        answer = x + 5\n"
                f"        return answer  {EM}← Use return, not print{NORM}\n"
                f"\n"
                f"  Remember: {EM}return{NORM} gives the value back to the caller.\n"
                f"            {EM}print(){NORM} just shows it on screen.\n"
            )
            return result, message

    return result, None


# ============================================================================
# Progress tracking hooks
# ============================================================================


class ProgressTracker:
    """Track test results for generating trace.json."""

    def __init__(self):
        self.results = []
        self.current_set = None

    def add_result(self, name: str, passed: bool):
        """Add a test result."""
        self.results.append({"name": name, "value": 1 if passed else 0})

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of results."""
        total = sum(r["value"] for r in self.results)
        return {"mark": total, "of_total": len(self.results), "results": self.results}


# Global progress tracker instance
_progress_tracker = ProgressTracker()


@pytest.fixture(scope="session")
def progress_tracker():
    """Provide access to the progress tracker."""
    return _progress_tracker


# ============================================================================
# Pytest hooks for custom behavior
# ============================================================================


def pytest_collection_modifyitems(config, items):
    """Modify collected test items.

    This hook allows us to add markers, modify test order, etc.
    """
    for item in items:
        # Add set marker based on file path
        if "set1" in str(item.fspath):
            item.add_marker(pytest.mark.set1)
        elif "set2" in str(item.fspath):
            item.add_marker(pytest.mark.set2)
        elif "set3" in str(item.fspath):
            item.add_marker(pytest.mark.set3)
        elif "set4" in str(item.fspath):
            item.add_marker(pytest.mark.set4)
        elif "set5" in str(item.fspath):
            item.add_marker(pytest.mark.set5)
        elif "set8" in str(item.fspath):
            item.add_marker(pytest.mark.set8)


def pytest_runtest_makereport(item, call):
    """Hook to track test results for progress tracking."""
    if call.when == "call":
        passed = call.excinfo is None
        _progress_tracker.add_result(item.name, passed)


def pytest_sessionfinish(session, exitstatus):
    """Hook called after test session finishes.

    This is where we can generate trace.json and show celebration messages.
    """
    # Get test results
    passed = session.testscollected - session.testsfailed
    total = session.testscollected

    # Show summary
    print(f"\n\n{'='*60}")
    print(f"Results: {passed}/{total} tests passed")

    # Show celebration if all passed
    if passed == total and total > 0:
        print(
            f"\n{Fore.GREEN}🎉 Perfect score! All tests passed! 🎉{Style.RESET_ALL}\n"
        )
        print(nyan_cat())
    elif passed > 0:
        print(
            f"\n{Fore.YELLOW}Keep going! You've got {passed} passing!{Style.RESET_ALL}"
        )
        print(f"✨🌟✨ I believe in you! ✨🌟✨\n")

    print(f"{'='*60}\n")


# ============================================================================
# Helper functions that can be imported by test files
# ============================================================================


def get_set_number_from_path(test_file_path: str) -> int:
    """Extract set number from a test file path.

    Example: /path/to/set2/test_exercise1.py -> 2
    """
    parts = Path(test_file_path).parts
    for part in parts:
        if part.startswith("set") and part[3:].isdigit():
            return int(part[3:])
    return 0
