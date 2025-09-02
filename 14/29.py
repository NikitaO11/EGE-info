def f(n,p):
    s=[]
    while n>0:
        s += [n%p]
        n//=p
    sp = s[::-1]
    return sp
x = 39*15**64+35**450+74*43**121-450035
max8=0
for p in range(9,100):
    m=list(map(str,f(x,p)))
    print(p,m.count("8"))