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
