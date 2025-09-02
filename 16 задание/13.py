from functools import*
from sys import*
setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n<=3:
        return n
    if n>3 and n%2==0:
        return 2*n*n+f(n-1)
    if n>3 and n%2!=0:
        return n*n*n+n+f(n-1)
k=0
for n in range(1,10000):
    if f(n)<10**7:
        k+=1
    print(k)