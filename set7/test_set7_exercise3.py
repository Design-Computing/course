"""Test Set 7 Exercise 3 - Advanced Python."""

import pytest
from collections import Counter, defaultdict


@pytest.fixture
def exercise3(load_exercise):
    """Load exercise 3."""
    return load_exercise(7, 3)


class TestDictComprehensions:
    """Test dictionary comprehension exercises."""

    def test_create_pet_length_dict(self, exercise3, pets):
        """Test creating a dict of pet names to lengths."""
        result = exercise3.create_pet_length_dict()
        expected = {pet: len(pet) for pet in pets}

        assert result == expected, (
            f"💡 Use a dictionary comprehension\n"
            f"Hint: {{pet: len(pet) for pet in pets}}\n\n"
            f"Expected 'dog': {expected['dog']}\n"
            f"Got 'dog': {result.get('dog', 'missing') if result else 'None'}"
        )

    def test_create_number_square_dict(self, exercise3):
        """Test creating a dict of numbers to squares."""
        result = exercise3.create_number_square_dict()
        expected = {n: n**2 for n in range(10)}

        assert result == expected, (
            f"💡 Use a dictionary comprehension with range()\n"
            f"Hint: {{n: n**2 for n in range(10)}}\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_create_first_letter_dict(self, exercise3, pets):
        """Test creating a dict of first letters to pet names."""
        result = exercise3.create_first_letter_dict()

        # Build expected: first occurrence of each letter
        expected = {}
        for pet in pets:
            letter = pet[0]
            if letter not in expected:
                expected[letter] = pet

        assert isinstance(result, dict), f"Expected dict, got {type(result)}"

        # Check that all letters in result are valid first letters
        for letter, pet in result.items():
            assert pet.startswith(letter), (
                f"💡 Each pet should start with its key letter\n"
                f"Key '{letter}' has value '{pet}' which doesn't start with '{letter}'"
            )

        # The result should have one pet per unique first letter
        unique_first_letters = len(set(p[0] for p in pets))
        assert len(result) == unique_first_letters, (
            f"💡 Should have one entry per unique first letter\n"
            f"Expected {unique_first_letters} entries\n"
            f"Got {len(result)} entries"
        )

    def test_filter_dict_comprehension(self, exercise3, pets):
        """Test filtering in a dict comprehension."""
        result = exercise3.filter_dict_comprehension()
        expected = {pet: len(pet) for pet in pets if len(pet) > 8}

        assert result == expected, (
            f"💡 Add a condition to the dict comprehension\n"
            f"Hint: {{pet: len(pet) for pet in pets if len(pet) > 8}}\n\n"
            f"Expected {len(expected)} entries\n"
            f"Got {len(result) if result else 0} entries"
        )


class TestGenerators:
    """Test generator exercises."""

    def test_count_up_generator(self, exercise3):
        """Test count up generator."""
        result = list(exercise3.count_up_generator(1, 5))
        expected = [1, 2, 3, 4, 5]

        assert result == expected, (
            f"💡 Use yield to generate each number\n"
            f"Example:\n"
            f"    for i in range(start, end + 1):\n"
            f"        yield i\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_fibonacci_generator(self, exercise3):
        """Test Fibonacci generator."""
        result = list(exercise3.fibonacci_generator(10))
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        assert result == expected, (
            f"💡 Generate Fibonacci numbers using yield\n"
            f"Start with a=0, b=1, yield a\n"
            f"Then loop: yield b, a, b = b, a+b\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_even_numbers_generator(self, exercise3):
        """Test even numbers generator."""
        result = list(exercise3.even_numbers_generator(20))
        expected = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

        assert result == expected, (
            f"💡 Use yield to generate even numbers\n"
            f"Hint: yield numbers from 0 to max_num where number % 2 == 0\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_infinite_counter(self, exercise3):
        """Test infinite counter generator."""
        gen = exercise3.infinite_counter()

        # Test first 5 values
        result = [next(gen) for _ in range(5)]
        expected = [0, 1, 2, 3, 4]

        assert result == expected, (
            f"💡 Create a generator that counts forever\n"
            f"Hint: Use a while True loop with yield\n\n"
            f"Expected first 5: {expected}\n"
            f"Got first 5:      {result}"
        )

        # Test it continues counting
        assert next(gen) == 5, "Generator should continue counting"


class TestCounter:
    """Test Counter exercises."""

    def test_count_first_letters(self, exercise3, pets):
        """Test counting first letters."""
        result = exercise3.count_first_letters()
        expected = Counter([p[0] for p in pets])

        assert result == expected, (
            f"💡 Use Counter to count first letters\n"
            f"Hint: Counter([p[0] for p in pets])\n\n"
            f"Expected 'g' count: {expected['g']}\n"
            f"Got 'g' count:      {result.get('g', 0) if result else 0}"
        )

    def test_count_number_frequency(self, exercise3):
        """Test counting number frequency."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise3")
        numbers = ex.numbers

        result = exercise3.count_number_frequency()
        expected = Counter(numbers)

        assert isinstance(result, Counter), f"Expected Counter, got {type(result)}"

        # Check a few values match
        for num in list(set(numbers))[:5]:
            assert result[num] == expected[num], (
                f"💡 Use Counter to count number frequencies\n"
                f"Hint: Counter(numbers)\n\n"
                f"Number {num} appears {expected[num]} times\n"
                f"But you counted {result[num]} times"
            )

    def test_most_common_number(self, exercise3):
        """Test finding the most common number."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise3")
        numbers = ex.numbers

        result = exercise3.most_common_number()
        expected = Counter(numbers).most_common(1)[0]

        assert result == expected, (
            f"💡 Use Counter().most_common(1)[0]\n"
            f"This returns the (value, count) tuple for the most common item\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_top_three_letters(self, exercise3, pets):
        """Test finding top 3 most common first letters."""
        result = exercise3.top_three_letters()
        expected = Counter([p[0] for p in pets]).most_common(3)

        assert result == expected, (
            f"💡 Use Counter().most_common(3)\n"
            f"Hint: Counter([p[0] for p in pets]).most_common(3)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )


class TestDefaultdict:
    """Test defaultdict exercises."""

    def test_group_pets_by_first_letter(self, exercise3, pets):
        """Test grouping pets by first letter."""
        result = exercise3.group_pets_by_first_letter()

        # Build expected groups
        expected = defaultdict(list)
        for pet in pets:
            expected[pet[0]].append(pet)

        assert isinstance(result, dict), f"Expected dict, got {type(result)}"

        # Check all letters are present
        for letter in expected:
            assert letter in result, (
                f"💡 Missing letter '{letter}' in result\n"
                f"Hint: Use defaultdict(list) and group[pet[0]].append(pet)"
            )

            assert result[letter] == expected[letter], (
                f"💡 Pets for letter '{letter}' don't match\n"
                f"Expected: {expected[letter]}\n"
                f"Got:      {result[letter]}"
            )

    def test_group_pets_by_length(self, exercise3, pets):
        """Test grouping pets by name length."""
        result = exercise3.group_pets_by_length()

        # Build expected groups
        expected = defaultdict(list)
        for pet in pets:
            expected[len(pet)].append(pet)

        assert isinstance(result, dict), f"Expected dict, got {type(result)}"

        # Check all lengths are present
        for length in expected:
            assert length in result, (
                f"💡 Missing length {length} in result\n"
                f"Hint: Use defaultdict(list) and group[len(pet)].append(pet)"
            )

            assert result[length] == expected[length], (
                f"💡 Pets with length {length} don't match\n"
                f"Expected: {expected[length]}\n"
                f"Got:      {result[length]}"
            )

    def test_count_with_defaultdict(self, exercise3, pets):
        """Test counting with defaultdict(int)."""
        result = exercise3.count_with_defaultdict()

        # Build expected counts
        expected = defaultdict(int)
        for pet in pets:
            expected[pet[0]] += 1

        assert isinstance(result, dict), f"Expected dict, got {type(result)}"

        # Check all counts match
        for letter in expected:
            assert letter in result, f"💡 Missing letter '{letter}' in counts"

            assert result[letter] == expected[letter], (
                f"💡 Count for letter '{letter}' doesn't match\n"
                f"Expected: {expected[letter]}\n"
                f"Got:      {result[letter]}\n\n"
                f"Hint: Use defaultdict(int) and counts[pet[0]] += 1"
            )


class TestBonusChallenges:
    """Test bonus challenge exercises."""

    def test_lazy_evaluation_demo(self, exercise3):
        """Test lazy evaluation with large generator."""
        gen = exercise3.lazy_evaluation_demo()

        # Should return a generator, not a list
        from collections.abc import Generator

        assert isinstance(gen, Generator), (
            f"💡 Should return a generator, not a list!\n"
            f"Expected: Generator\n"
            f"Got:      {type(gen)}\n\n"
            f"Hint: Just yield the squares, don't convert to list"
        )

        # Test first few values
        result = [next(gen) for _ in range(5)]
        expected = [0, 1, 4, 9, 16]

        assert result == expected, (
            f"💡 Generator should yield squares of 0, 1, 2, 3, ...\n"
            f"Expected first 5: {expected}\n"
            f"Got first 5:      {result}"
        )

    def test_chain_generators(self, exercise3):
        """Test chaining generator operations."""
        result = exercise3.chain_generators()
        expected = [x**2 for x in range(1, 101) if x % 2 == 0]

        assert result == expected, (
            f"💡 Chain multiple generator operations:\n"
            f"1. Generate 1-100\n"
            f"2. Filter for even numbers\n"
            f"3. Square each even number\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_word_length_histogram_prep(self, exercise3, pets):
        """Test preparing data for a histogram."""
        result = exercise3.word_length_histogram_prep()
        expected = Counter([len(p) for p in pets])

        assert isinstance(result, Counter), f"Expected Counter, got {type(result)}"

        assert result == expected, (
            f"💡 Count how many pets have each name length\n"
            f"Hint: Counter([len(p) for p in pets])\n\n"
            f"This gives you the data for a histogram:\n"
            f"x-axis: name length, y-axis: count of pets with that length\n\n"
            f"Expected: {dict(expected)}\n"
            f"Got:      {dict(result) if result else 'None'}"
        )
