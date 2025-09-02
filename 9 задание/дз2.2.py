f = open("дз2.txt")
k=0
for line in f:
    a = sorted(list(map(int,line.split())))
    if (a[0]+a[3])%2!=0 and (a[1]+a[2])%2!=0:
        if a[0]+a[3]==a[1]+a[2]:
            k+=1
print(k)
