from sys import*
from functools import*
setrecursionlimit(100000000)
@lru_cache(None)
def f(n):
    if n<20:
        return n
    if n>=20:
        return (n-6)*f(n-7)
for n in range(48000):
    f(n)

print((f(47872)-290*f(47865))/f(47858))