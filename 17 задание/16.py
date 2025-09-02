f = open("17-16.txt")
a = [int(x) for x in f]
nch=[x for x in a if x%2!=0]
nch1=sum(nch)/len(nch)
res=[]
for i in range(0,len(a)-2):
    if (a[i]%3)!=(a[i+1]%3) and (a[i]%3)!=(a[i+2]%3) and (a[i+1]%3)!=(a[i+2]%3):
        if (a[i]<nch1)+(a[i+1]<nch1)+(a[i+2]<nch1)==1:
            summ = a[i]+a[i+1]+a[i+2]
            res.append(summ)
print(len(res),max(res))




