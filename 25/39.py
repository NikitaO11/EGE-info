def deln(n):
    res=[]
    flag=False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            flag=True
            res.append(i)
            if n//i!=i:
                res.append(n//i)
    if flag==False:
        return 0
    else:
        return res

for n in range(800001,850000):
    if deln(n)!=0:
        m = min(deln(n))+max(deln(n))
        if m%10==4:
            print(n,m)

