def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    return False

def delp(n):
    res=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    return res
for n in range(550001,560000):
    sp = delp(n)
    if len(sp)>0:
        mx = max(sp)
        if prost(mx):
            print(n,mx)