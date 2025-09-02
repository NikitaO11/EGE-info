def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def delprost(n):
    d=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if prost(i):
                d.append(i)
            if i!= n//i and prost(n//i):
                d.append(n//i)
    return d
k=0
for n in range(2,20000+1):
    sp = delprost(n)
    if len(sp)>3:
        k+=1
        print(k)