f = open("9-3.txt")
k=0
for i in f:
    a = list(map(int,i.split()))
    a = sorted(a)
    if (a[0]*a[1]==a[2]*a[3])+(a[0]*a[2]==a[1]*a[3])+(a[0]*a[3]==a[2]*a[1])>=1:
        if (a[2]*a[2]) > max(a)*min(a):
            k+=1
        print(k)