def f(a,b,c):
    if a>b: return 0
    if a==b and c<=2: return 1
    if c==2: return f(a+1,b,c)
    return f(a+1,b,c)+f(a*2,b,c+1)
print(f(1,11,0))