"""Test Set 5 Exercise 2 - ABBA pattern and Koch curves."""

import pytest


@pytest.fixture
def exercise2(load_exercise):
    """Load exercise 2."""
    return load_exercise(5, 2)


class TestABBA:
    """Test the ABBA recursion pattern."""

    @pytest.mark.parametrize(
        "source,count,expected",
        [
            ("baaab", 2, "bbaoaaobaobaobbbaaobaobbbaaobaobbbabbaoaaob"),
            ("b", 2, "bbaoaaob"),
            ("roof", 2, "roabbaoabbaf"),
            ("hell", 2, "hell"),
        ],
    )
    def test_abba(self, exercise2, source, count, expected):
        """Test ABBA pattern recursion."""
        result = exercise2.abba(source, count)
        assert result == expected, (
            f"ABBA pattern failed!\n"
            f"Input:    {source!r} (count={count})\n"
            f"Expected: {expected!r}\n"
            f"Got:      {result!r}"
        )


class TestKochCurves:
    """Test Koch curve drawing functions."""

    def test_draw_square(self, exercise2):
        """Test Koch square pattern _|-|_."""
        result = exercise2.draw_square(2)
        expected = "2100000100000100000100000100000"
        assert result == expected, (
            f"Koch square pattern (_|-|_) failed!\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_draw_pointy(self, exercise2):
        """Test Koch pointy pattern _^_."""
        result = exercise2.draw_pointy(2)
        expected = "210000100001000010000"
        assert result == expected, (
            f"Koch pointy pattern (_^_) failed!\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )
