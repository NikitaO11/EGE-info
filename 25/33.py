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
            if i != n//i and prost(n//i):
                res.append(n//i)
    return res
for n in range(550001,560000):
    sp = delp(n)
    if len(sp)>0:
        if sum(sp)%10==1:
            print(n,sum(sp))
