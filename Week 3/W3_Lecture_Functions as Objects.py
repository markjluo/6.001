def applyToEach(L, f):
    """Apply the function to each element in the list"""
    for i in range(len(L)):
        L[i] = f(L[i])


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result







L = [1, -2, 3.4]

print(applyToEach(L, abs))

print(applyToEach(L, int))

print(applyToEach(L, factorial))

print(applyToEach(L, fib))

# ==========================================================================================


def applyFuns2(L, x):
    """Apply all functions in the list  to integer x"""
    for f in L:
        print(f(x))


print(applyFuns2([abs, int, factorial, fib], 4))


# ==========================================================================================
# Generation of Higher Order Procedure (HOP) (map)
# - Python provides a general purpose HOP, map
# - Simple form - a unary function (a function that expects only one argument) and
# a collection of suitable arguments
map(abs, [1, -2, 3, -4])

# Produces an 'iterable', so need to walk it down
for elt in map(abs, [1,-2, 3, 4]):
    print(elt)

# General form with N-ary functions:
L1 = [1, 28, 36]
L2 = [2, 57, 9]
map(min, L1, L2)
for elt in map(min, L1, L2):
    print(elt)
# This returns the minimum of the two lists in each place

