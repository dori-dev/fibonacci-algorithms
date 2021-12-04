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


def performance_test(numbers: int, codes: str, setup: str) -> None:
    """test the performance of this fibonacci algorithm

    Args:
        numbers (int): fibonacci numbers
        codes (str): run codes
        setup (str): setup codes
    """
    if test_fibonacci():
        print('Correct Algorithm!')
    else:
        print('Incorrect Algorithm!')
        return
    print(getsizeof(numbers), 'bytes.')
    print('time', timeit(codes, setup=setup, number=1000))
