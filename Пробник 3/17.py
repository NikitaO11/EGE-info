f = open("17-1.txt")
a = [int(x) for x in f]
res=[]
for i in range(len(a)-2):
    if (len((str((a)[i])))==5 and abs(a[i])%100==43) + (len((str((a)[i+1])))==5 and abs(a[i])%100==43) + (len((str((a)[i+2])))==5 and abs(a[i])%100==43)>=1:
        if len((str((a)[i])))==5 and abs(a[i])%100==43 and a[i]>a[i+1] and a[i]>a[i+2]:
            if ((a[i+1])**2) + ((a[i+2])**2) <= ((a[i])**2):
                sum1 = a[i]+a[i+1]+a[i+2]
                res.append(sum1)
        if len((str((a)[i+1])))==5 and abs(a[i])%100==43 and a[i+1]>a[i] and a[i+1]>a[i+2]:
            if (a[i]**2) + (a[i+2]) <= a[i+1]**2:
                sum2 = a[i]+a[i+1]+a[i+2]
                res.append(sum2)
        if len((str((a)[i+2])))==5 and abs(a[i])%100==43 and a[i+2]>a[i] and a[i+2]>a[i+1]:
            if (a[i]**2) + (a[i+1]**2) <= a[i+2]**2:
                sum3 = a[i]+a[i+1]+a[i+2]
                res.append(sum3)
print(len(res),min(res))


