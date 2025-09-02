f = open("17-25.txt")
a=[int(x) for x in f]
mina = [x for x in a if x%2!=0]
mina = min(mina)
res=[]
for i in range(len(a)-1):
    if (a[i]%3==0)+(a[i+1]%3==0)==1:
        s = a[i]-a[i+1]
        s = abs(s)
        if s<mina:
            res.append(s)
print(len(res),max(res))
