# Recursion may be simpler, more intuitive
# Recursion may be efficient from a programmer's point of view,
# but may not be efficient from a computer's point of view

def factorial_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n)
