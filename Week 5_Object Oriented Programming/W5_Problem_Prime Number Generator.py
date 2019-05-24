def genPrimes():
    P = [2]
    yield 2
    e = 2
    while True:
        e += 1
        isPrime = True
        for p in P:
            if e % p == 0:
                isPrime = False
        if isPrime:
            P.append(e)
            yield e

a = genPrimes()

print(a.__next__())
print(a.__next__())
print(a.__next__())