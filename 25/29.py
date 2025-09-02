def delp(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return n//i+i
    return 0
for n in range(800000,1000000):
    if delp(n)!=0 and delp(n)%10==8:
        print(n,delp(n))

