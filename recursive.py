"""fibonacci with recursive functions
"""

from sys import getsizeof
from timeit import timeit


def fibonacci(number: int) -> int:
    """calculate the fibonacci number of this index

   Args:
        number(int): index of fibonacci numbers

    Returns:
        int: fibonacci number
    """

    if number in {0, 1}:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

def test_fibonacci() -> bool:


    fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = []
    for number in range(len(fib_numbers)):
        result.append(fibonacci(number))

    return result == fib_numbers