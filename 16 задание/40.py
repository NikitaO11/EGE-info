from sys import*
from functools import*
setrecursionlimit(1000000)
@lru_cache(None)
def f(n):
    if n==1: return 3
    if n>1: return 2*n+5+f(n-1)
for n in range(1,10000):
    f(n)
print(f(3026)-f(3024))
