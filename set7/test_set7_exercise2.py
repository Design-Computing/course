"""Test Set 7 Exercise 2 - Functional Programming."""

import pytest


@pytest.fixture
def exercise2(load_exercise):
    """Load exercise 2."""
    return load_exercise(7, 2)


class TestLambdaFunctions:
    """Test lambda functions with sorted."""

    def test_sort_pets_by_length(self, exercise2, pets):
        """Test sorting pets by name length."""
        result = exercise2.sort_pets_by_length()
        expected = sorted(pets, key=lambda p: len(p))

        assert result == expected, (
            f"💡 Use sorted() with a lambda key function\n"
            f"Hint: sorted(pets, key=lambda p: len(p))\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_sort_pets_by_last_letter(self, exercise2, pets):
        """Test sorting pets by last letter."""
        result = exercise2.sort_pets_by_last_letter()
        expected = sorted(pets, key=lambda p: p[-1])

        assert result == expected, (
            f"💡 Use sorted() with a lambda that gets the last letter\n"
            f"Hint: sorted(pets, key=lambda p: p[-1])\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_sort_pets_reverse_alphabetical(self, exercise2, pets):
        """Test reverse alphabetical sort."""
        result = exercise2.sort_pets_reverse_alphabetical()
        expected = sorted(pets, reverse=True)

        assert result == expected, (
            f"💡 Use sorted() with reverse=True\n"
            f"Hint: sorted(pets, reverse=True)\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )


class TestMapFunction:
    """Test map function exercises."""

    def test_map_double_numbers(self, exercise2):
        """Test doubling numbers with map."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.map_double_numbers()
        expected = list(map(lambda x: x * 2, numbers))

        assert result == expected, (
            f"💡 Use map() with a lambda to double each number\n"
            f"Hint: list(map(lambda x: x * 2, numbers))\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_map_pet_lengths(self, exercise2, pets):
        """Test getting pet name lengths with map."""
        result = exercise2.map_pet_lengths()
        expected = list(map(len, pets))

        assert result == expected, (
            f"💡 Use map() with the len function\n"
            f"Hint: list(map(len, pets))\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_map_first_letter(self, exercise2, pets):
        """Test getting first letters with map."""
        result = exercise2.map_first_letter()
        expected = list(map(lambda p: p[0], pets))

        assert result == expected, (
            f"💡 Use map() with a lambda to get the first character\n"
            f"Hint: list(map(lambda p: p[0], pets))\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_map_uppercase(self, exercise2, pets):
        """Test converting to uppercase with map."""
        result = exercise2.map_uppercase()
        expected = list(map(str.upper, pets))

        assert result == expected, (
            f"💡 Use map() with str.upper or lambda p: p.upper()\n"
            f"Hint: list(map(str.upper, pets))\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )


class TestFilterFunction:
    """Test filter function exercises."""

    def test_filter_long_names(self, exercise2, pets):
        """Test filtering for long names."""
        result = exercise2.filter_long_names()
        expected = list(filter(lambda p: len(p) > 10, pets))

        assert result == expected, (
            f"💡 Use filter() with a lambda that checks length\n"
            f"Hint: list(filter(lambda p: len(p) > 10, pets))\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_filter_even_numbers(self, exercise2):
        """Test filtering for even numbers."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.filter_even_numbers()
        expected = list(filter(lambda x: x % 2 == 0, numbers))

        assert result == expected, (
            f"💡 Use filter() with a lambda that checks if even\n"
            f"Hint: list(filter(lambda x: x % 2 == 0, numbers))\n\n"
            f"First 5 expected: {expected[:5]}\n"
            f"First 5 got:      {result[:5] if result else 'None'}"
        )

    def test_filter_pets_with_space(self, exercise2, pets):
        """Test filtering for pets with spaces in names."""
        result = exercise2.filter_pets_with_space()
        expected = list(filter(lambda p: " " in p, pets))

        assert result == expected, (
            f"💡 Use filter() with a lambda that checks for space\n"
            f"Hint: list(filter(lambda p: ' ' in p, pets))\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )


class TestBuiltinFunctions:
    """Test built-in function exercises."""

    def test_find_longest_pet_name(self, exercise2, pets):
        """Test finding the longest pet name."""
        result = exercise2.find_longest_pet_name()
        expected = max(pets, key=len)

        assert result == expected, (
            f"💡 Use max() with key=len\n"
            f"Hint: max(pets, key=len)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_find_shortest_pet_name(self, exercise2, pets):
        """Test finding the shortest pet name."""
        result = exercise2.find_shortest_pet_name()
        expected = min(pets, key=len)

        assert result == expected, (
            f"💡 Use min() with key=len\n"
            f"Hint: min(pets, key=len)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_find_max_number(self, exercise2):
        """Test finding the maximum number."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.find_max_number()
        expected = max(numbers)

        assert result == expected, (
            f"💡 Use max() to find the largest number\n"
            f"Hint: max(numbers)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_find_min_number(self, exercise2):
        """Test finding the minimum number."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.find_min_number()
        expected = min(numbers)

        assert result == expected, (
            f"💡 Use min() to find the smallest number\n"
            f"Hint: min(numbers)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_sum_all_numbers(self, exercise2):
        """Test summing all numbers."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.sum_all_numbers()
        expected = sum(numbers)

        assert result == expected, (
            f"💡 Use sum() to add all numbers\n"
            f"Hint: sum(numbers)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    def test_average_number(self, exercise2):
        """Test calculating the average."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.average_number()
        expected = sum(numbers) / len(numbers)

        assert result == expected, (
            f"💡 Average = sum / count\n"
            f"Hint: sum(numbers) / len(numbers)\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )


class TestZipFunction:
    """Test zip function exercises."""

    def test_zip_pets_with_numbers(self, exercise2, pets):
        """Test zipping pets with numbers."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.zip_pets_with_numbers()
        expected = list(zip(pets, numbers))

        assert result == expected, (
            f"💡 Use zip() to combine two sequences\n"
            f"Hint: list(zip(pets, numbers))\n\n"
            f"First 3 expected: {expected[:3]}\n"
            f"First 3 got:      {result[:3] if result else 'None'}"
        )

    def test_create_pet_dictionary(self, exercise2, pets):
        """Test creating a dictionary from zip."""
        # Get the numbers list from the module
        from importlib import import_module

        ex = import_module("set7.exercise2")
        numbers = ex.numbers

        result = exercise2.create_pet_dictionary()
        expected = dict(zip(pets, numbers))

        assert result == expected, (
            f"💡 Convert zipped tuples to a dict\n"
            f"Hint: dict(zip(pets, numbers))\n\n"
            f"First 3 keys: {list(expected.keys())[:3]}\n"
            f"Got these keys: {list(result.keys())[:3] if result else 'None'}"
        )


class TestEnumerateFunction:
    """Test enumerate function exercises."""

    def test_enumerate_pets(self, exercise2, pets):
        """Test enumerating pets."""
        result = exercise2.enumerate_pets()
        expected = list(enumerate(pets))

        assert result == expected, (
            f"💡 Use enumerate() to get (index, value) pairs\n"
            f"Hint: list(enumerate(pets))\n\n"
            f"First 3 expected: {expected[:3]}\n"
            f"First 3 got:      {result[:3] if result else 'None'}"
        )

    def test_enumerate_from_one(self, exercise2, pets):
        """Test enumerating from 1."""
        result = exercise2.enumerate_from_one()
        expected = list(enumerate(pets, start=1))

        assert result == expected, (
            f"💡 Use enumerate() with start=1\n"
            f"Hint: list(enumerate(pets, start=1))\n\n"
            f"First 3 expected: {expected[:3]}\n"
            f"First 3 got:      {result[:3] if result else 'None'}"
        )

    def test_find_pet_positions(self, exercise2, pets):
        """Test finding positions of pets starting with 'g'."""
        result = exercise2.find_pet_positions()
        expected = [i for i, p in enumerate(pets) if p.startswith("g")]

        assert result == expected, (
            f"💡 Use enumerate in a list comprehension\n"
            f"Hint: [i for i, p in enumerate(pets) if p.startswith('g')]\n\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )
