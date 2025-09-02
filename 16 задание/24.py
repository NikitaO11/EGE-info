from sys import*
from functools import*
setrecursionlimit(10000000)
@lru_cache(None)
def f(n):
    if n<=3:
        return n
    if n>3 and n%2==0:
        return 2*n*n+f(n-1)
    if n>3 and n%2!=0:
        return n*n*n+n+f(n-1)
k = 0
for n in range(1,100000):
    if f(n)<10000000:
        k+=1
print(k)


