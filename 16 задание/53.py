from sys import*
from functools import*
setrecursionlimit(1000000)
@lru_cache(None)

def f(n):
    if n>=5000:
        return n
    if n<5000:
        return n*2+f(n+2)

for n in range(5000,-1,-1):
    f(n)
print(f(82)-f(81))
