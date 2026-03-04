# -*- coding: UTF-8 -*-
"""Tests for Set 2 lab book completion.

Checks that students have filled out their readme.md reflection.
"""

import pytest


@pytest.mark.set2
def test_lab_book_entry_completed(lab_book_completed):
    """Test that the lab book (readme.md) has been filled out.
    
    Students should reflect on what they learned and what's still unclear.
    """
    completed = lab_book_completed(set_number=2)
    
    assert completed, (
        "📝 Lab book not completed!\n"
        "Please fill out set2/readme.md with your reflections on this week's work.\n"
        "What did you learn? What's still unclear?"
    )
