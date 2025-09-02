from sys import*
from functools import*
setrecursionlimit(1000000)
@lru_cache(None)
def f(n):
    if n==1: return 1
    if n>1: return n*f(n-1)
for n in range(1,10000):
    f(n)
print(((f(2025)//25)+f(2024))//f(2023))