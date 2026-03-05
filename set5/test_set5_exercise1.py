"""Test Set 5 Exercise 1 - Word API and recursion."""

import pytest


@pytest.fixture
def exercise1(load_exercise):
    """Load exercise 1."""
    return load_exercise(5, 1)


def test_word_length(word, requested_length, expected_length):
    """Check that word lengths are as expected.

    Requesting a word less than 3 chars long should fail.
    """
    if isinstance(requested_length, str) and word is not None:
        pytest.fail(
            "❌ This API returns a random word if you malform the url.\n"
            "You'll need to typecheck the input. I.e. check:\n"
            "    if type(length) is int:\n"
            "        # and so on\n"
            "It also does the same thing if you go under 3 characters\n"
            "long, so remember to check for that too!"
        )
    if expected_length is None and word is None:
        return True
    if word is None:
        return False
    if len(word) == requested_length and len(word) == expected_length:
        return True
    pytest.fail(
        f"Something odd happened: word={word}, requested={requested_length}, expected={expected_length}"
    )


class TestWordAPI:
    """Test the word API functions."""

    @pytest.mark.parametrize(
        "length,expected_length",
        [
            (5, 5),  # Normal case
            (8, 8),  # Different length
            (4, 4),  # Minimum valid length (API restriction)
            (0, None),  # Invalid: too short, should return None
            ("a", None),  # Invalid: not an int, should return None
        ],
    )
    def test_get_a_word_of_length_n(self, exercise1, length, expected_length):
        """Test getting a word of specific length from API."""
        word = exercise1.get_a_word_of_length_n(length)

        if expected_length is None:
            assert (
                word is None
            ), f"Expected None for invalid input {length}, got: {word}"
        else:
            assert (
                word is not None
            ), f"Expected a word of length {expected_length}, got None"
            assert (
                len(word) == expected_length
            ), f"Expected word of length {expected_length}, got length {len(word)}: '{word}'"
            assert test_word_length(word, length, expected_length)

    @pytest.mark.parametrize(
        "lengths",
        [
            [4, 5, 6],  # Ascending
            [4, 18, 4],  # With variation
        ],
    )
    def test_list_of_words_with_lengths(self, exercise1, lengths):
        """Test getting a list of words with specified lengths."""
        words = exercise1.list_of_words_with_lengths(lengths)

        assert (
            words is not None
        ), f"Expected list of words for lengths {lengths}, got None"
        assert isinstance(words, list), f"Expected list, got {type(words)}"
        assert len(words) == len(
            lengths
        ), f"Expected {len(lengths)} words, got {len(words)}"

        for word, expected_len in zip(words, lengths):
            assert (
                len(word) == expected_len
            ), f"Expected word of length {expected_len}, got length {len(word)}: '{word}'"
