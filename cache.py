"""fibonacci with recursive functions and cache
"""


# Standart library imports
from sys import getsizeof
from timeit import timeit


cache = {
    0: 0,
    1: 1
}


def fibonacci(number: int) -> int:
    """calculate fibonacci of the number

   Args:
        number(int): number with calculate it fibonacci

    Returns:
        int: fibonacci(number - 1) + fibonacci(number -2)  recursive case
    """
    if number not in cache:
        cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
    return cache[number]
