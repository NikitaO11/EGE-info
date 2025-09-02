from functools import*
from sys import*
setrecursionlimit(100000)
@lru_cache(None)

def f(n):
    if n>=1000:
        return 1000
    if n<1000 and n%2!=0:
        return n*f(n+1)
    if n<1000 and n%2==0:
        return n*f(n+1)/2
print(f(998)//f(1001))