from sys import setrecursionlimit

setrecursionlimit(1000000000000)
def f(n):
    if n==1:
        return 1
    if n>1:
        return (4*n+7)*f(n-1)+16
count=0
for k in range(10**12,2*10**12+1):
    if f(k)%2==0:
        count+=1
    print(count)