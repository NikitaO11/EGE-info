f = open("ПРОБНИК_02_1_задание17.txt")
a = [int(x) for x in f]
max_2 = [x for x in a if 10<=x<=99]
max_2=max(max_2)
res=[]
for i in range(len(a)-1):
    if (10<=a[i]<=99)+(10<=a[i+1]<=99)==1:
        if (a[i]+a[i+1])%int(max_2)==0:
            s=a[i]+a[i+1]
            res.append(s)
print(len(res),max(res))
