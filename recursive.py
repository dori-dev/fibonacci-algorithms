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
    """test the fibonacci function

    Returns:
        bool: True if `fibonacci` currect work else False
    """

    fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = []
    for number in range(len(fib_numbers)):
        result.append(fibonacci(number))

    return result == fib_numbers


def optimization_test(numbers: int, codes: str, setup: str) -> bool:
    """test the optimization of this fibonacci algorithm

    Args:
        numbers (int): fibonacci numbers
        codes (str): run codes
        setup (str): setup codes
    """
    if test_fibonacci():
        print('Correct algorithm!')
    else:
        print('Incorrect algorithm!')
        return

    print(getsizeof(numbers), 'bytes.')

    print('time', timeit(codes, setup=setup, number=1000))
