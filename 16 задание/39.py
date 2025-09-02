from sys import*
from functools import*
setrecursionlimit(10000000)
@lru_cache(None)
def f(n):
    if n<10: return n**n
    if n>=10: return (n-1)*f(n-2)
for n in range(1,100000):
    f(n)
print((f(34652)-250*f(34650))//f(34648))