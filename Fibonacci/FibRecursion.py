# Recursion method to calculate fibonacci. Savees memory but can use a lot of processing
# Do not try to get a big fib number (50)
def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(50))