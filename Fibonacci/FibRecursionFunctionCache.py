# This func will memo all outputs from functions calls
from functools import lru_cache

# Define no limit for the cache of the memo function
@lru_cache(maxsize=None)

def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(100))