"""Test Set 6 Exercise 1 - Refactoring wordy_pyramid."""

import pytest


@pytest.fixture
def exercise1(load_exercise):
    """Load exercise 1."""
    return load_exercise(6, 1)


@pytest.fixture
def set5_exercise1(load_exercise):
    """Load set 5 exercise 1 for helper functions."""
    return load_exercise(5, 1)


class TestRefactoring:
    """Test the refactored wordy_pyramid function."""

    def test_wordy_pyramid_refactored(self, exercise1, set5_exercise1):
        """Test that wordy_pyramid uses list_of_words_with_lengths from set 5."""
        import inspect

        source = inspect.getsource(exercise1.wordy_pyramid)

        # Check that they're using the helper function
        assert "list_of_words_with_lengths" in source, (
            "💡 You should refactor wordy_pyramid to use list_of_words_with_lengths from set 5!\n"
            "This demonstrates the DRY (Don't Repeat Yourself) principle.\n\n"
            "Hint: Import it at the top:\n"
            "    from set5.exercise1 import list_of_words_with_lengths\n\n"
            "Then use it to get all the words instead of repeating the API call logic."
        )

        # Check that they're not repeating the requests code
        assert source.count("requests.get") <= 1, (
            "💡 You should reduce code duplication!\n"
            "If you're calling requests.get multiple times in wordy_pyramid,\n"
            "you're repeating yourself. Use list_of_words_with_lengths instead."
        )

    @pytest.mark.api_call
    @pytest.mark.timeout(30)
    def test_wordy_pyramid_output(self, exercise1):
        """Test that wordy_pyramid returns the correct pyramid of words."""
        expected_lengths = [
            3,
            5,
            7,
            9,
            11,
            13,
            15,
            17,
            19,
            20,
            18,
            16,
            14,
            12,
            10,
            8,
            6,
            4,
        ]

        words = exercise1.wordy_pyramid()
        assert words is not None, "wordy_pyramid returned None"
        assert isinstance(words, list), f"Expected list, got {type(words)}"

        actual_lengths = [len(w) for w in words]
        assert actual_lengths == expected_lengths, (
            f"Word length pyramid incorrect!\n"
            f"Expected: {expected_lengths}\n"
            f"Got:      {actual_lengths}\n\n"
            f"Words: {', '.join([f'{w} ({len(w)})' for w in words])}"
        )

    def test_code_is_cleaner(self, exercise1):
        """Test that the refactored code is cleaner than the original."""
        import inspect

        source = inspect.getsource(exercise1.wordy_pyramid)
        lines = [
            line
            for line in source.split("\n")
            if line.strip() and not line.strip().startswith("#")
        ]

        # The refactored version should be much shorter
        assert len(lines) < 20, (
            f"💡 Your refactored function has {len(lines)} non-empty lines.\n"
            "A well-refactored version should be under 20 lines.\n"
            "Try using the helper functions more effectively!"
        )
