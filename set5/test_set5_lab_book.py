"""Test Set 5 Lab Book completion."""

import pytest


def test_lab_book_entry_completed(lab_book_completed):
    """Check that the lab book has been updated."""
    assert lab_book_completed(5), (
        "📓 You haven't updated your lab book!\n"
        "Please document what you learned in week 5."
    )
