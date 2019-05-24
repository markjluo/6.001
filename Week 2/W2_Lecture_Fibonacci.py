def fib(n):
    """assumes n an int >= 0
            returns Fibonacci of n"""
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
