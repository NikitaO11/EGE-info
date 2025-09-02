from sys import*
setrecursionlimit(100000)
def f(n):
    if n>=2025:
        return n
    if n<2025:
        return f(n+2)+n
print(f(2022)-f(2023))