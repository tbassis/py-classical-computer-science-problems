# Most efficient functino to calculate the value of fibonacci among the files in this project

def fib(n: int) -> int:
    if n == 0: return n # especial case

    last: int = 0 # base value for fib(0)
    next: int = 1 # base value for fib(1)

    for _ in range(1, n):
        # Unpacking tuples will update variable values after calculate new values
        last, next = next, last + next
    
    return next

if __name__ == '__main__':
    print(fib(150))