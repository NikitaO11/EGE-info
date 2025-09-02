f = open("пробник №01_06_задание17.txt")
a = [int(x) for x in f]
min1 = min(a)
res=[]
for i in range(len(a)-1):
    if (a[i]%27==min1)+(a[i+1]%27==min1)>=1:
        s = a[i]+a[i+1]
        res.append(s)
print(len(res),max(res))

