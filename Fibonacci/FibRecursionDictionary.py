from typing import Dict

# create a dictionary with the base cases
memory: Dict[int, int] = {0: 0, 1: 1} 

# fib use recursion, but since it has a dictionary, some values wont be needed to be recalculated anymore
def fib(n: int) -> int:
    if n not in memory:
        memory[n] = fib(n - 1) + fib(n - 2)
    return memory[n]


if __name__ == '__main__':
    print(fib(50))