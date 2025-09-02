def cc(x):
    s=''
    while x>0:
        s=str(x%3) + s
        x=x//3
    return s
for n in range(1,200):
    n2=cc(n)
    if n%3 == 0:
        n2 = "1" + n2 + "02"
    else:
        n2 = n2 + cc(n%3*4)
    r=int(n2,3)
    if r<=199:
        print(n,r)