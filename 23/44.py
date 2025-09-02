def f(a,b):
    if a>b: return 0
    if a==b: return 1
    if a<b:
        if a==15 or a==14:
            return f(a+2,b)
        else:
            return f(a+1,b)+f(a+2,b)
print(f(3,18))