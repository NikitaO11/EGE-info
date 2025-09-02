def f(a,b):
    if a<b or a==24: return 0
    if a==b: return 1
    if a>b: return f(a-1,b)+f(a-6,b)+f(a//2,b)
print(f(34,20)*f(20,19)*f(19,6))