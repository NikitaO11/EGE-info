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
for n in range(25317,51237+1):
    sp = delprost(n)
    if len(sp)>=6:
        print(n,sp)