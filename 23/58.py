def f(a,b,k):
    if a>b: return 0
    if a==b and k<=5: return 1
    if a<b: return f(a+1,b,k)+f(a*3,b,k+1)+f(a*4,b,k+1)
print(f(3,300,0))