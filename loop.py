"""fibonacci with for loop
"""

# Standart library imports
from sys import getsizeof
from timeit import timeit


def fibonacci(number):

    if not (isinstance(number, int) and number >= 0):
        raise ValueError("Please enter a positive interger!")

    first, second = 0, 1
    data = []
    for _ in range(1, number+1):
        data.append(first)
        first, second = second, first + second

    return data
