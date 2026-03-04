# -*- coding: UTF-8 -*-
"""Test for Set 4 lab book completion."""

import pytest


@pytest.mark.set4
def test_lab_book_entry_completed(lab_book_completed):
    """Test that the lab book (readme.md) has been filled out."""
    completed = lab_book_completed(set_number=4)
    
    assert completed, (
        "📝 Lab book not completed!\n"
        "Please fill out set4/readme.md with your reflections on this week's work."
    )
