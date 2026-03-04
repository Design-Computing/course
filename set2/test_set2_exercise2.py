# -*- coding: UTF-8 -*-
"""Tests for Set 2, Exercise 2.

This exercise comes with syntax errors that students need to fix.
"""

import pytest


@pytest.mark.exercise2
@pytest.mark.set2
def test_exercise2_runs(check_exercise_runs):
    """Test that exercise 2 runs without syntax errors.
    
    Note: This exercise intentionally comes with errors that students must fix!
    """
    runs = check_exercise_runs(set_number=2, exercise_number=2)
    
    if not runs:
        pytest.fail(
            "Exercise 2 has syntax errors that need to be fixed!\n"
            "Don't worry - this is expected. Exercise 2 comes with errors "
            "and it's your job to fix them. 🔧"
        )
    
    assert runs, "Exercise 2 should run without syntax errors once fixed"
