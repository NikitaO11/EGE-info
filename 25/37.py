def delp(n):
    res=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    return res

for n in range(123456789,223456789+1):
    sp=delp(n)
    if len(sp)==3:
        print(n,max(sp))