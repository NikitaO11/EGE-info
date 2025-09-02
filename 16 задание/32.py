from sys import*
setrecursionlimit(100000)
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
print(f(2023)//f(2020))