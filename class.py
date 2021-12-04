"""fibonacci with recursive class and cache
"""

# Standart library imports
from sys import getsizeof
from timeit import timeit


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, number):
        if number >= len(self.cache):
            self.cache.append(self(number - 1) + self(number - 2))
        return self.cache[number]

    def test_fibonacci(self) -> bool:
        """test the fibonacci function

        Returns:
            bool: True if `fibonacci` currect work else False
        """
        fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        result = []
        for number in range(len(fib_numbers)):
            result.append(self(number))
        return fib_numbers == result

    def performance_test(self, numbers: int, codes: str, setup: str) -> None:
        """test the performance of this fibonacci algorithm

        Args:
            numbers (int): fibonacci numbers
            codes (str): run codes
            setup (str): setup codes
        """
        if self.test_fibonacci():
            print('Correct Algorithm!')
        else:
            print('Incorrect Algorithm!')
            return
        print(getsizeof(numbers), 'bytes.')
        print('time', timeit(codes, setup=setup, number=1000))


fibonacci = Fibonacci()

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


SETUP = '''class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, number):
        if number >= len(self.cache):
            self.cache.append(self(number - 1) + self(number - 2))
        return self.cache[number]

fibonacci = Fibonacci()

counts = [1, 0, 20, 15, 10, 2, 5, 9, 4]
index = 0
'''


fibonacci.performance_test(fibonacci_numbers, RUN, SETUP)
