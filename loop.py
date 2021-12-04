"""fibonacci with for loop
"""

# Standart library imports
from sys import getsizeof
from timeit import timeit


def fibonacci(number):
    first, second = 0, 1
    data = []
    for _ in range(1, number+1):
        data.append(first)
        first, second = second, first + second

    return data


def test_fibonacci() -> bool:
    """test the fibonacci function

    Returns:
        bool: True if `fibonacci` currect work else False
    """
    fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = []
    for number in range(len(fib_numbers)):
        result.append(fibonacci(number))
    return fib_numbers == result
