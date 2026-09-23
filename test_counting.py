import pytest
from counting import find_max, count_even

@pytest.mark.parametrize("numbers", "expected", [([1,2,3], 3), ([9,12,21], 21)])
def test_find_max(numbers, expected):
    assert find_max(numbers) == expected

@pytest.mark.parametrize("num", "exp", [([2,3,4], 2), ([2,4,6], 3)])
def test_count_even(num, exp):
    assert count_even(num) == exp