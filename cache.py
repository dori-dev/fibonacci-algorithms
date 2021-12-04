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


COUNT = 10
if not (isinstance(COUNT, int) and COUNT >= 0):
    raise ValueError("Please enter a positive interger!")
fibonacci_numbers = (fibonacci(number) for number in range(COUNT))
print('fibonacci(10) ->', *fibonacci_numbers)


RUN = '''
fibonacci_numbers = (fibonacci(number) for number in range(counts[index]))
data = list(fibonacci_numbers)
index += 1
if index == len(counts):
    index = 0
'''


SETUP = '''def fibonacci(number: int) -> int:
    """calculate the fibonacci number of this index

   Args:
        number(int): index of fibonacci numbers

    Returns:
        int: fibonacci number
    """

    if number in {0, 1}:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

counts = [1, 0, 20, 15, 10, 2, 5, 9, 4]
index = 0
'''
