def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def delp(n):
    res=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if prost(i):
                res.append(i)
            if i!=i//n and prost(n//i):
                res.append(n//i)
    return res

for n in range(1200001,1250000):
    sp=delp(n)
    if len(sp)>0:
        m = max(sp)+min(sp)
        if m>2000 and m%10==8:
            print(n,m)