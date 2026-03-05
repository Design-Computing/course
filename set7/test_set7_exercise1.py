"""Test Set 7 Exercise 1 - List Operations and Comprehensions."""

import pytest
from importlib import import_module


@pytest.fixture
def exercise1(load_exercise):
    """Load exercise 1."""
    return load_exercise(7, 1)


class TestSlicing:
    """Test list slicing operations."""

    def test_first_ten_pets(self, exercise1, pets):
        """Test getting first 10 pets."""
        result = exercise1.first_ten_pets()
        expected = pets[:10]

        assert result == expected, (
            f"💡 Use slicing to get the first 10 pets\n"
            f"Hint: pets[:10]\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_last_five_pets(self, exercise1, pets):
        """Test getting last 5 pets."""
        result = exercise1.last_five_pets()
        expected = pets[-5:]

        assert result == expected, (
            f"💡 Use negative indexing to get the last 5 pets\n"
            f"Hint: pets[-5:]\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_pets_from_4_to_10(self, exercise1, pets):
        """Test getting pets from index 4 to 10."""
        result = exercise1.pets_from_4_to_10()
        expected = pets[4:10]

        assert result == expected, (
            f"💡 Use slicing with start and end indices\n"
            f"Hint: pets[4:10] (end index is exclusive)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_middle_pets(self, exercise1, pets):
        """Test getting middle 20 pets."""
        result = exercise1.middle_pets()
        expected = pets[10:30]

        assert result == expected, (
            f"💡 Get the middle 20 pets (skip first 10, take next 20)\n"
            f"Hint: pets[10:30]\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    @pytest.mark.parametrize(
        "list_length",
        [
            20,  # Edge case: exactly 20 items (entire list)
            21,  # Odd, just over minimum
            22,  # Even, just over minimum
            40,  # Original case, even
            41,  # Original case + 1, odd
            50,  # Larger even
            67,  # Larger odd
            100,  # Large even
        ],
    )
    def test_moving_middle_pets(self, exercise1, pets, list_length, monkeypatch):
        """Test getting middle 20 pets from lists of various lengths."""
        # Create a test list of the specified length
        # Duplicate and slice the pets list to get desired length
        repetitions = (list_length // len(pets)) + 1
        test_pets = (pets * repetitions)[:list_length]

        # Patch the pets list in the exercise module
        ex = import_module("set7.exercise1")
        monkeypatch.setattr(ex, "pets", test_pets)

        # Call the function
        result = exercise1.moving_middle_pets()

        # Should return list of 20 items
        assert isinstance(result, list), f"Expected list, got {type(result)}"
        assert len(result) == 20, (
            f"💡 Should return exactly 20 items (list_length={list_length})\n"
            f"Expected length: 20\n"
            f"Got length:      {len(result)}"
        )

        # Calculate expected middle 20
        start = (list_length - 20) // 2
        end = start + 20
        expected = test_pets[start:end]

        assert result == expected, (
            f"💡 Calculate indices based on list length\n"
            f"For a list of {list_length}, middle 20 should start at index {start}\n"
            f"Hint: start = (len(pets) - 20) // 2\n"
            f"      end = start + 20\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_reverse_pets(self, exercise1, pets):
        """Test reversing the pets list."""
        result = exercise1.reverse_pets()
        expected = pets[::-1]

        assert result == expected, (
            f"💡 Use slicing with step -1 to reverse a list\n"
            f"Hint: pets[::-1]\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_every_third_pet(self, exercise1, pets):
        """Test getting every third pet."""
        result = exercise1.every_third_pet()
        expected = pets[::3]

        assert result == expected, (
            f"💡 Use slicing with step 3\n"
            f"Hint: pets[::3]\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )


class TestAppendExtend:
    """Test append and extend operations."""

    def test_append_example(self, exercise1):
        """Test appending single items."""
        result = exercise1.append_example()
        expected = ["cat", "dog", "hamster", "rabbit"]

        assert result == expected, (
            f"💡 Use .append() to add single items\n"
            f"my_pets.append('hamster')\n"
            f"my_pets.append('rabbit')\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_extend_example(self, exercise1):
        """Test extending with multiple items."""
        result = exercise1.extend_example()
        expected = ["cat", "dog", "hamster", "rabbit", "guinea pig", "mouse"]

        assert result == expected, (
            f"💡 Use .extend() to add multiple items from a list\n"
            f"my_pets.extend(['hamster', 'rabbit'])\n"
            f"my_pets.extend(['guinea pig', 'mouse'])\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_append_vs_extend_comparison(self, exercise1):
        """Test the difference between append and extend."""
        result = exercise1.append_vs_extend_comparison()

        assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
        assert len(result) == 2, f"Expected tuple of 2 lists, got {len(result)} items"

        list1, list2 = result

        # list1 should have a nested list
        expected_list1 = [["cat", "dog"]]
        # list2 should be flat
        expected_list2 = ["cat", "dog"]

        assert list1 == expected_list1, (
            f"💡 list1 should use .append() which adds the list as a single item\n"
            f"list1.append(['cat', 'dog'])\n\n"
            f"Expected: {expected_list1}\n"
            f"Got:      {list1}"
        )

        assert list2 == expected_list2, (
            f"💡 list2 should use .extend() which adds each item from the list\n"
            f"list2.extend(['cat', 'dog'])\n\n"
            f"Expected: {expected_list2}\n"
            f"Got:      {list2}"
        )


class TestListComprehensions:
    """Test list comprehension exercises."""

    def test_pet_name_lengths(self, exercise1, pets):
        """Test getting lengths of pet names."""
        result = exercise1.pet_name_lengths()
        expected = [len(p) for p in pets]

        assert result == expected, (
            f"💡 Use a list comprehension to get lengths\n"
            f"Hint: [len(p) for p in pets]\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_long_pet_names(self, exercise1, pets):
        """Test filtering for long pet names."""
        result = exercise1.long_pet_names()
        expected = [p for p in pets if len(p) > 10]

        assert result == expected, (
            f"💡 Use a list comprehension with a condition\n"
            f"Hint: [p for p in pets if len(p) > 10]\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_pet_names_uppercase(self, exercise1, pets):
        """Test converting pet names to uppercase."""
        result = exercise1.pet_names_uppercase()
        expected = [p.upper() for p in pets]

        assert result == expected, (
            f"💡 Use a list comprehension with .upper()\n"
            f"Hint: [p.upper() for p in pets]\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_pets_starting_with_g(self, exercise1, pets):
        """Test filtering pets starting with 'g'."""
        result = exercise1.pets_starting_with_g()
        expected = [p for p in pets if p.startswith("g")]

        assert result == expected, (
            f"💡 Use a list comprehension with .startswith()\n"
            f"Hint: [p for p in pets if p.startswith('g')]\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_pet_name_and_length(self, exercise1, pets):
        """Test creating tuples of name and length."""
        result = exercise1.pet_name_and_length()
        expected = [(p, len(p)) for p in pets]

        assert result == expected, (
            f"💡 Use a list comprehension to create tuples\n"
            f"Hint: [(p, len(p)) for p in pets]\n\n"
            f"First 3 expected: {expected[:3]}\n"
            f"First 3 got:      {result[:3] if result else 'None'}"
        )


class TestBonusChallenges:
    """Test bonus challenge exercises."""

    def test_nested_list_comprehension(self, exercise1):
        """Test creating a 5x5 grid with nested comprehensions."""
        result = exercise1.nested_list_comprehension()

        # Check structure
        assert isinstance(result, list), f"Expected list, got {type(result)}"
        assert len(result) == 5, f"Expected 5 rows, got {len(result)}"

        for i, row in enumerate(result):
            assert isinstance(row, list), f"Row {i} should be a list, got {type(row)}"
            assert len(row) == 5, f"Row {i} should have 5 items, got {len(row)}"

        # Check values
        expected = [[f"({i},{j})" for j in range(5)] for i in range(5)]

        assert result == expected, (
            f"💡 Use nested list comprehensions\n"
            f"Hint: [[f'({i},{j})' for j in range(5)] for i in range(5)]\n\n"
            f"Expected first row: {expected[0]}\n"
            f"Got first row:      {result[0] if result else 'None'}"
        )
