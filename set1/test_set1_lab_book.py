# -*- coding: UTF-8 -*-
"""Test for Set 1 lab book completion."""

import pytest


@pytest.mark.set1
def test_lab_book_entry_completed(lab_book_completed):
    """Test that the lab book (readme.md) has been filled out."""
    completed = lab_book_completed(set_number=1)
    
    assert completed, (
        "📝 Lab book not completed!\n"
        "Please fill out set1/readme.md with your reflections on this week's work.\n"
        "What did you learn? What's still unclear?"
    )
