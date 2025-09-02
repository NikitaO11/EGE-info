def f(n):
    s=""
    while n>0:
        s = str(n%9)+s
        n//=9
    return s
x = 2*729**2019+2*243**2020-81**2021+2*27**2022-2*9**2023-2024
print(len(f(x))-f(x).count("0"))
