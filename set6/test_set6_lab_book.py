"""Test Set 6 Lab Book."""

import pytest


@pytest.mark.set6
def test_lab_book_entry_completed(lab_book_completed):
    """Test that the lab book has been completed."""
    completed = lab_book_completed(set_number=6)
    assert completed, (
        "📝 Lab book not completed!\n"
        "Please fill out set6/readme.md with your reflections on this week's work.\n"
        "What did you learn about refactoring? How does it improve your code?"
    )
