def f(a,b,k):
    if a>b: return 0
    if a==b and k==1: return 1
    if k==1: return f(a+1,b,k)+f(a+2,b,k)
    return f(a+1,b,k)+f(a+2,b,k)+f(a*2,b,k+1)+f(a*3,b,k+1)
print(f(1,11,0))