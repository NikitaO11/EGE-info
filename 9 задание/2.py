f = open("9-2.txt")
k=0
for i in f:
    a = list(map(int,i.split()))
    a = sorted(a)
    if a[3]<a[0]+a[1]+a[2]:
        if (a[0]+a[1]==a[2]+a[3])+(a[0]+a[2]==a[1]+a[3])+(a[0]+a[3]==a[2]+a[1])>=1:
            k+=1
        print(k)