a=0
for n in range(1,100):
    n2=bin(n)[2:]
    if sum(map(int,n2))%2 == 0:
        n2 += "0"
    else:
        n2 += "1"
    if sum(map(int,n2))%2 == 0:
        n2 += "0"
    else:
        n2 += "1"
    r=int(n2,2)
    if 210<=r<=260:
        a+=1
        print(r,a)
