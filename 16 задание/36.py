from sys import*
from functools import*
setrecursionlimit(10000000)
@lru_cache(None)
def f(n):
    if n<=3: return n
    if n>3 and n%2==0: return f(n-1)+2*f(n//2)
    if n>3 and n%2!=0: return f(n-1)+f(n-3)
k=0
for n in range(1,10000):
    if f(n)<10**8:
        k+=1
print(k)
