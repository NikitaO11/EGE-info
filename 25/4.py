from fnmatch import*
def f(n):
    s=0
    while n>0:
        s+=n%10
        n=n//10
    return s
for i in range(0,10**8+1,2024):
    if fnmatch(str(i),"1?4*78*") and sum(map(int,str(i)))<35:
        if f(i)<35:
            print(i)