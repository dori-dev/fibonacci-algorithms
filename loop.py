"""fibonacci with for loop
"""

# Standart library imports
from sys import getsizeof
from timeit import timeit


def fibonacci(number: int) -> list:
    """calculate the fibonacci numbers from 0 to number

   Args:
        number(int): index of fibonacci numbers

    Returns:
        list: list of fibonacci numbers
    """
    first, second = 0, 1
    result = []
    for _ in range(1, number+1):
        result.append(first)
        first, second = second, first + second
    return result


def test_fibonacci() -> bool:
    """test the fibonacci function

    Returns:
        bool: True if `fibonacci` currect work else False
    """
    fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = fibonacci(len(fib_numbers))
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


COUNT = 10
if not (isinstance(COUNT, int) and COUNT >= 0):
    raise ValueError("Please enter a positive interger!")
fibonacci_numbers = fibonacci(COUNT)
print('fibonacci(10) ->', *fibonacci_numbers)


RUN = '''
fibonacci_numbers = fibonacci(counts[index])
index += 1
if index == len(counts):
    index = 0
'''


SETUP = '''def fibonacci(number: int) -> list:
    """calculate the fibonacci numbers from 0 to number

   Args:
        number(int): index of fibonacci numbers

    Returns:
        list: list of fibonacci numbers
    """
    first, second = 0, 1
    result = []
    for _ in range(1, number+1):
        result.append(first)
        first, second = second, first + second
    return result
counts = [1, 0, 20, 15, 10, 2, 5, 9, 4]
index = 0
'''

performance_test(fibonacci_numbers, RUN, SETUP)
