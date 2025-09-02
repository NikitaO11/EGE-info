from sys import*
setrecursionlimit(1000000)
def f(n):
    if n<11:
        return 10
    if n>=11:
        return n+f(n-1)
print(f(2124)-f(2122))