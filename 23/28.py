def f(a,b):
    if a>b or a==38: return 0
    if a==b: return 1
    if a<b: return f(a+2,b)+f(a*2,b)
print(f(2,20)*f(20,44))