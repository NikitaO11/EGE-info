def f(a,b,k):
    if k==2:
        return 0
    if a>b: return 0
    if a==b: return 1
    if a<b: return f(a+1,b,0)+f(a+2,b,0)+f(a*2,b,k+1)
print(f(1,11,0))
