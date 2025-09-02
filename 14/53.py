def f(n):
    s=""
    while n>0:
        s = str(n%9)+s
        n//=9
    return s
res=[]
for x in range(5769,0,-1):
    m = 9**2025+9**1000-x
    if f(m).count("0")==1026:
        print(x)
        break