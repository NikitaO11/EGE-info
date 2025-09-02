def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def delprost(n):
    res=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if prost(i):
                res.append(i)
            if i!=n//i and prost(n//i):
                res.append(n//i)
    return res
for n in range(25317,51237+1):
    sp = delprost(n)
    if len(sp)>=6:
        print(n,max(sp))