"""Test Set 8 - Final Exam (Exercise 1337)."""

import inspect
import os
import string
import pytest


TIMEOUT_SECONDS = 3


@pytest.fixture
def exam(check_exercise_runs, load_exercise):
    """Load the exam exercise (1337)."""
    if not check_exercise_runs(8, 1337):
        pytest.skip("Exercise 1337 file doesn't run")
    return load_exercise(8, 1337)


class TestSimpleReturns:
    """Test basic return value requirements."""

    def test_give_me_five(self, exam):
        """Test give_me_five returns 5."""
        result = exam.give_me_five()
        assert result == 5, (
            "💡 Don't over think this! Just return the number 5!\n"
            f"Expected: 5\n"
            f"Got:      {result}"
        )

    def test_password_please(self, exam):
        """Test password_please returns a valid password string."""
        result = exam.password_please()

        assert isinstance(result, str), f"Expected string, got {type(result)}"
        assert (
            result.upper() != result.lower()
        ), "Password must contain letters (not just symbols/numbers)"
        assert (
            len(result) >= 8
        ), f"Password must be at least 8 characters, got {len(result)}"

    def test_list_please(self, exam):
        """Test list_please returns a list."""
        result = exam.list_please()
        assert isinstance(result, list), (
            "💡 Don't over think this! Just return a list!\n"
            f"Expected: list\n"
            f"Got:      {type(result)}"
        )

    def test_int_list_please(self, exam):
        """Test int_list_please returns a list of integers."""
        result = exam.int_list_please()

        assert isinstance(result, list), f"Expected list, got {type(result)}"
        assert all(isinstance(i, int) for i in result), (
            "💡 All elements must be integers!\n"
            f"Got types: {[type(i).__name__ for i in result]}"
        )

    def test_string_list_please(self, exam):
        """Test string_list_please returns a list of strings."""
        result = exam.string_list_please()

        assert isinstance(result, list), f"Expected list, got {type(result)}"
        assert all(isinstance(i, str) for i in result), (
            "💡 All elements must be strings!\n"
            f"Got types: {[type(i).__name__ for i in result]}"
        )

    def test_dictionary_please(self, exam):
        """Test dictionary_please returns a dictionary."""
        result = exam.dictionary_please()
        assert isinstance(result, dict), (
            "💡 Don't over think this! Just return a dictionary!\n"
            f"Expected: dict\n"
            f"Got:      {type(result)}"
        )


class TestIsIt5:
    """Test the is_it_5 function."""

    @pytest.mark.parametrize(
        "input_val,expected",
        [
            (5, True),
            (4, False),
            ("cats", False),
        ],
    )
    def test_is_it_5(self, exam, input_val, expected):
        """Test is_it_5 with various inputs."""
        result = exam.is_it_5(input_val)
        assert result == expected, (
            f"is_it_5({input_val!r})\n" f"Expected: {expected}\n" f"Got:      {result}"
        )


class TestTakeFive:
    """Test the take_five function."""

    @pytest.mark.parametrize(
        "input_val,expected",
        [
            (5, 0),  # 5 - 5 = 0
            (10, 5),  # 10 - 5 = 5
            (0, -5),  # 0 - 5 = -5
        ],
    )
    def test_take_five(self, exam, input_val, expected):
        """Test take_five subtracts 5."""
        result = exam.take_five(input_val)
        assert result == expected, (
            f"take_five({input_val})\n" f"Expected: {expected}\n" f"Got:      {result}"
        )


class TestGreet:
    """Test the greet function."""

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("the Queen", "Well hello, the Queen"),
            ("Pr♂nc♀♂", "Well hello, Pr♂nc♀♂"),
        ],
    )
    def test_greet(self, exam, name, expected):
        """Test greet function with various names."""
        result = exam.greet(name)
        assert result == expected, (
            f"greet({name!r})\n" f"Expected: {expected!r}\n" f"Got:      {result!r}"
        )


class TestCounters:
    """Test counting functions."""

    @pytest.mark.parametrize(
        "input_list,expected",
        [
            ([1, 1, 1, 3, 3], 3),
            ([0, 1, 2, 5, -9], 1),
        ],
    )
    def test_one_counter(self, exam, input_list, expected):
        """Test one_counter counts 1s in a list."""
        result = exam.one_counter(input_list)
        assert result == expected, (
            f"one_counter({input_list})\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    @pytest.mark.parametrize(
        "n,input_list,expected",
        [
            (7, [], 0),
            (4, [4, 0, 4], 2),
            (0, [0, 0, 0, "0", "zero"], 3),  # Only count actual 0s, not strings
        ],
    )
    def test_n_counter(self, exam, n, input_list, expected):
        """Test n_counter counts occurrences of n."""
        result = exam.n_counter(n, input_list)
        assert result == expected, (
            f"n_counter({n}, {input_list})\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )


def test_fizz_buzz(exam):
    """Test FizzBuzz implementation."""
    # fmt: off
    expected = [
        1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 
        13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, 
        "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, 
        "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, 
        "FizzBuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", 
        "Buzz", 56, "Fizz", 58, 59, "FizzBuzz", 61, 62, "Fizz", 64, "Buzz", 
        "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "FizzBuzz", 76, 
        77, "Fizz", 79, "Buzz", "Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 
        88, 89, "FizzBuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, 
        "Fizz", "Buzz",
    ]
    # fmt: on

    result = exam.fizz_buzz()
    assert result == expected, (
        "FizzBuzz implementation incorrect!\n"
        "Remember:\n"
        "  - Divisible by 15 → 'FizzBuzz'\n"
        "  - Divisible by 3 → 'Fizz'\n"
        "  - Divisible by 5 → 'Buzz'\n"
        "  - Otherwise → the number\n"
        f"\nFirst few items:\n"
        f"Expected: {expected[:15]}\n"
        f"Got:      {result[:15] if len(result) >= 15 else result}"
    )


class TestSetItOnFire:
    """Test the set_it_on_fire function."""

    @pytest.mark.parametrize(
        "input_str,expected,emoji_hint",
        [
            ("this disco", "🔥T🔥H🔥I🔥S🔥 🔥D🔥I🔥S🔥C🔥O🔥", "🛼🕺🧑‍🎤👨‍🎤👩‍🎤🕺🛼"),
            ("💥💥💥", "🔥💥🔥💥🔥💥🔥", "💣"),
            (
                "💖my heart💖",
                "🔥💖🔥M🔥Y🔥 🔥H🔥E🔥A🔥R🔥T🔥💖🔥",
                "💖💘💝💖💗💓💞😻😍🥰❤️🧡💛💚💙💜🤎🖤🤍🫀",
            ),
        ],
    )
    def test_set_it_on_fire(self, exam, input_str, expected, emoji_hint):
        """Test set_it_on_fire adds fire emoji between characters."""
        result = exam.set_it_on_fire(input_str)
        assert result == expected, (
            f"{emoji_hint}\n"
            f"set_it_on_fire({input_str!r})\n"
            f"Expected: {expected!r}\n"
            f"Got:      {result!r}"
        )


class TestChainGang:
    """Test the_chain_gang_5 function and its implementation."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (10, True),
            (11, False),
            (9, True),
        ],
    )
    def test_the_chain_gang_5(self, exam, n, expected):
        """Test the_chain_gang_5 returns True if n is divisible by 5."""
        result = exam.the_chain_gang_5(n)
        assert result == expected, (
            f"⛓️⛓️⛓️⛓️⛓️\n"
            f"the_chain_gang_5({n})\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_chain_gang_no_equality_operator(self, exam):
        """Test that the_chain_gang_5 doesn't use == operator (except in docstring)."""
        source = inspect.getsource(exam.the_chain_gang_5)
        count = source.count("==")

        assert count == 1, (
            "🦹‍♀️⛓️🦹‍♀️⛓️🦹‍♀️\n"
            f"The way you've written the_chain_gang_5 contains {count} instances of '==',\n"
            "but it should contain 1 (which is in the docstring/function definition).\n"
            "💡 Hint: You can check divisibility without using == !"
        )

    def test_chain_gang_no_subtraction(self, exam):
        """Test that the_chain_gang_5 doesn't use - operator (except in docstring)."""
        source = inspect.getsource(exam.the_chain_gang_5)
        count = source.count("-")

        assert count == 2, (
            "🦹‍♀️⛓️🦹‍♀️⛓️🦹‍♀️\n"
            f"The way you've written the_chain_gang_5 contains {count} instances of '-',\n"
            "but it should contain 2 (which are in the docstring/function definition).\n"
            "💡 Hint: Use the modulo operator % instead of subtraction!"
        )


class TestPetFilter:
    """Test pet filtering functions."""

    @pytest.mark.parametrize(
        "letter,expected",
        [
            ("x", ["red fox"]),
            ("q", []),
            (
                "p",
                [
                    "pig",
                    "sheep",
                    "guinea pig",
                    "python",
                    "scorpion",
                    "pigeon",
                    "alpaca",
                    "guppy",
                ],
            ),
        ],
    )
    def test_pet_filter(self, exam, letter, expected):
        """Test pet_filter returns pets containing the letter."""
        result = exam.pet_filter(letter)
        assert result == expected, (
            f"pet_filter({letter!r})\n" f"Expected: {expected}\n" f"Got:      {result}"
        )

    def test_best_letter_for_pets(self, exam):
        """Test best_letter_for_pets returns 'e'."""
        result = exam.best_letter_for_pets()
        assert result == "e", (
            f"best_letter_for_pets()\n" f"Expected: 'e'\n" f"Got:      {result!r}"
        )


class TestFillerText:
    """Test filler text generation functions."""

    def test_make_filler_text_dictionary(self, exam):
        """Test dictionary creation with words of specific lengths."""
        result = exam.make_filler_text_dictionary()

        assert isinstance(result, dict), f"Expected dict, got {type(result)}"

        # Check that we have the expected keys and word lengths
        expected_word_lengths = {
            "3": [3, 3, 3, 3],
            "4": [4, 4, 4, 4],
            "5": [5, 5, 5, 5],
            "6": [6, 6, 6, 6],
            "7": [7, 7, 7, 7],
        }

        for key, expected_lengths in expected_word_lengths.items():
            assert key in result, f"Missing key '{key}' in dictionary"
            words = result[key]
            actual_lengths = [len(w) for w in words]
            assert actual_lengths == expected_lengths, (
                f"Dictionary key '{key}' has incorrect word lengths:\n"
                f"Expected: {expected_lengths}\n"
                f"Got:      {actual_lengths}"
            )

    @pytest.mark.parametrize("word_count", [50, 1000])
    @pytest.mark.api_call
    def test_random_filler_text(self, exam, word_count):
        """Test random_filler_text generates text with correct word count."""
        result = exam.random_filler_text(word_count)

        assert isinstance(result, str), f"Expected str, got {type(result)}"
        words = result.split(" ")
        assert (
            len(words) == word_count
        ), f"Expected {word_count} words, got {len(words)}"
        assert len(result) > 3 * word_count, (
            f"Text seems too short - minimum expected length is {3 * word_count}, "
            f"got {len(result)}"
        )

    @pytest.mark.parametrize("word_count", [100, 10])
    def test_fast_filler_basics(self, exam, word_count):
        """Test fast_filler generates text with correct word count."""
        # Clean up any old cached file first
        dict_file = "dict_racey.json"
        if os.path.exists(dict_file):
            os.remove(dict_file)

        result = exam.fast_filler(word_count)

        assert isinstance(result, str), f"Expected str, got {type(result)}"
        words = result.split(" ")
        assert (
            len(words) == word_count
        ), f"Expected {word_count} words, got {len(words)}"
        assert len(result) > 3 * word_count, (
            f"Text seems too short - minimum expected length is {3 * word_count}, "
            f"got {len(result)}"
        )

    def test_fast_filler_capitalized(self, exam):
        """Test that fast_filler output starts with a capital letter."""
        result = exam.fast_filler(10)

        assert len(result) > 0, "fast_filler returned empty string"
        assert (
            result[0] in string.ascii_uppercase
        ), f"First character should be uppercase, got: '{result[0]}'"
        assert (
            result[1] in string.ascii_lowercase
        ), f"Second character should be lowercase, got: '{result[1]}'"

    def test_fast_filler_ends_with_period(self, exam):
        """Test that fast_filler output ends with a period."""
        result = exam.fast_filler(10)

        assert result.endswith("."), f"Output should end with '.', got: '{result[-1]}'"

    @pytest.mark.timeout(1)
    def test_fast_filler_performance(self, exam):
        """Test that fast_filler is actually fast (caching works).

        This test runs fast_filler 10 times and expects it to complete
        within 1 second total. This ensures the dictionary caching is working.
        """
        # Clean up first
        dict_file = "dict_racey.json"
        if os.path.exists(dict_file):
            os.remove(dict_file)

        # Run 10 times - should be fast due to caching
        for _ in range(10):
            result = exam.fast_filler(1000)
            assert len(result.split(" ")) == 1000

        # If we get here without timeout, caching is working!
        assert True, (
            "✨ Great! Your caching is working - all 10 iterations completed quickly!\n"
            "The pattern of saving a value locally so that you don't need to go\n"
            "and get it again is called caching."
        )
