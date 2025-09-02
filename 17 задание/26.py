f = open("17_1.5.txt")
a = [int(x) for x in f]
mina = [x for x in a if (-999<=x<=-100 or 100<=x<=999) and x%10==5]
mina = min(mina)
res=[]
for i in range(len(a)-1):
    if (100<=abs(a[i])<=999) or (100<=abs(a[i+1])<=999):
        s = a[i]+a[i+1]
        if s%mina==0:
            res.append(s)
print(len(res),max(res))