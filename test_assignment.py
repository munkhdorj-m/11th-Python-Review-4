import pytest
import inspect
from assignment import sum_even_odd, count_ending_with_5, factorial_list, count_occurrences

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source


# Exercise 1: Sum of even and odd numbers
@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3, 4, 5], [6, 9]),
    ([10, 11, 12, 13], [22, 24]),
    ([0, 1, 2], [2, 1]),
    ([5, 7, 9], [0, 21])
])
def test1(lst, expected):
    assert sum_even_odd(lst) == expected
    assert check_contains_loop(sum_even_odd)


# Exercise 2: Count numbers ending with 5
@pytest.mark.parametrize("lst, expected", [
    ([5, 15, 23, 25, 40], 3),
    ([1, 2, 3, 4, 6], 0),
    ([5, 55, 105], 3),
    ([10, 20, 30], 0)
])
def test2(lst, expected):
    assert count_ending_with_5(lst) == expected
    assert check_contains_loop(count_ending_with_5)


# Exercise 3: Factorial of each number in list
@pytest.mark.parametrize("lst, expected", [
    ([3, 4, 5], [6, 24, 120]),
    ([0, 1, 2], [1, 1, 2]),
    ([6, 3], [720, 6]),
    ([1, 1, 1], [1, 1, 1])
])
def test3(lst, expected):
    assert factorial_list(lst) == expected
    assert check_contains_loop(factorial_list)


# Exercise 4: Count occurrences of each number
@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 2, 3, 1, 4, 2], {1: 2, 2: 3, 3: 1, 4: 1}),
    ([5, 5, 5, 5], {5: 4}),
    ([1, 2, 3], {1: 1, 2: 1, 3: 1}),
    ([0, 0, 0, 1], {0: 3, 1: 1})
])
def test4(lst, expected):
    assert count_occurrences(lst) == expected
    assert check_contains_loop(count_occurrences)
