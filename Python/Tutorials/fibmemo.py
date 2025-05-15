def fibonacci(n):  
    return fibonacci_helper(n, dict())

def fibonacci_helper(n, fib_nums):
    if n in [0, 1]:
        return fib_nums.setdefault(n, n)

    fib1 = fib_nums.setdefault(n - 1, fibonacci_helper(n - 1, fib_nums))
    fib2 = fib_nums.setdefault(n - 2, fibonacci_helper(n - 2, fib_nums))

    return fib_nums.setdefault(n, fib1 + fib2)