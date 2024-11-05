def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def non_recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib1, fib2 = 0, 1
    for i in range(2, n + 1):
        next_fib = fib1 + fib2
        fib1, fib2 = fib2, next_fib
    return fib2

n = input("Enter a number to calculate Fibonacci: ")
n = int(n)
print(f"The {n}th Fibonacci number (Recursive): {recursive_fibonacci(n)}")
print(f"The {n}th Fibonacci number (Non-Recursive): {non_recursive_fibonacci(n)}")
