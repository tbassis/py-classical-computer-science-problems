# List all the values of fibonacci until reach de desirable value
from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
    yield 0

    if n > 0: yield 1

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        # Unpacking tuples will update variable values after calculate new values
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    for i in fib(10):
        print(i)