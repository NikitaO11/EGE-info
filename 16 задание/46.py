from sys import*
setrecursionlimit(100000)

def f(n):
    if n==1:
        return 1
    if n>1:
        return n*f(n-1)
print(f(446)//f(443))