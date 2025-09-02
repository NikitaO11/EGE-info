f = open("17-1.4.txt")
a = [int(x) for x in f]
res=[]
for i in range(len(a)-2):
    if (abs(a[i])%4==0)+(abs(a[i+1])%4==0)+(abs(a[i+2])%4==0)==3:
        if (abs(a[i])%14==0)+(abs(a[i+1])%14==0)+(abs(a[i+2])%14==0)>=1:
            sr = (a[i]+a[i+1]+a[i+2])//3
            res.append(sr)
print(len(res),min(res))