"""fibonacci with recursive class and cache
"""

# Standart library imports
from sys import getsizeof
from timeit import timeit


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, number):
        if number < len(self.cache):
            return self.cache[number]
        fib_number = self(number - 1) + self(number - 2)
        self.cache.append(fib_number)
        return self.cache[number]



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

COUNT = 10
if not (isinstance(COUNT, int) and COUNT >= 0):
    raise ValueError("Please enter a positive interger!")
fibonacci_numbers = (fibonacci(number) for number in range(COUNT))
print('fibonacci(10) ->', *fibonacci_numbers)
