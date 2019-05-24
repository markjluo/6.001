def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


# Method sometimes called "memoization"
def fib_efficient(n, d):
    # Access global variable to keep track of function calls
    global numFibCalls
    numFibCalls += 1
    # Can use the dictionary to hold onto values that I've already
    # computed that I don't need to recompute.
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


def fast_fib(n, memo={}):
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        try:
            return memo[n]
        except KeyError:
            result = fast_fib(n-1, memo) + fast_fib(n-2, memo)
            memo[n] = result
            return result




numFibCalls = 0
fibArg = 12

print(fib(fibArg))
print('funciton calls', numFibCalls)


numFibCalls = 0

d = {0: 1, 1:1}
print(fib_efficient(fibArg, d))
print('funciton calls', numFibCalls)


numFibCalls = 0
print(fast_fib(fibArg))
print('funciton calls', numFibCalls)