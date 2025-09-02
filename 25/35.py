def delp(n):
    res=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    return res

for n in range(800001,1000000):
    sp = sorted(delp(n))
    for i in range(0,len(sp)):
        if sp[i]!=7 and sp[i]%10==7:
            print(n,sp[i])
            break