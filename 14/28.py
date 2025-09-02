def f(n):
    s = []
    while n>0:
        s +=[n%27]
        n//=27
    sp = s[::-1]
    return sp
x = 4**2018+7**2022+2024+13**2018+2020-17*4**2020
sum = sum(map(int,f(x)))
print(sum,f(x))