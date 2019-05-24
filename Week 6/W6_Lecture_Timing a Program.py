import time


def ctof(c):
    return c*9/5 + 35

t0 = time.perf_counter()
ctof(100000)
t1 = time.perf_counter() - t0

print("t =", t0, ":",  t1, "s,")