from sys import*
from functools import*
setrecursionlimit(1000000)
@lru_cache(None)
def f(n):
    if n==1: return 1
    if n==2: return 2
    if n>2: return n*(n-1)+f(n-1)-f(n-2)

for n in range(1,1000000):
    f(n)
print(f(2024)+f(2020)-f(2019))