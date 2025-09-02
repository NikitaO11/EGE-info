f = open("17-9.txt")
a = [int(x) for x in f]
res = []
for i in range(len(a)-2):
    if (a[i]%14==0)+(a[i+1]%14==0)+(a[i+2]%14==0)>=1:
        if (a[i]%4==0)+(a[i+1]%4==0)+(a[i+2]%4==0)==3:
            s=a[i]+a[i+1]+a[i+2]
            res.append(s)
arif1=[]
for i in range(len(res)):
    arif = res[i]/3
    arif1.append(arif)
print(len(res),min(arif1))
