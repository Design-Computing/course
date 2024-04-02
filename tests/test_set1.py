"""Test Set 1"""

import sys
import os
import pytest

# Add the 'me' directory to the PYTHONPATH
ex_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "me", "set1")
)

sys.path.insert(0, ex_path)

import exercise1 as ex  # Now you can import your module


def test_obvs():
    assert True


def test_set_1_ex_1(capfd):
    """Test that s1x1 produces exactly "Hello world!"
    and offers suggestions abut how to improve.
    """
    ex.hello()
    out, err = capfd.readouterr()
    assert out.strip() == "Hello world!"
