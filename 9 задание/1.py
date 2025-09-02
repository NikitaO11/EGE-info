f = open("9-1(1).txt")
a=[]
k=0
for i in f:
    a = list(map(int,i.split()))
    b = sorted(a)
    if b[3] < b[0]+b[1]+b[2]:
        if (b[0]+b[1]!=b[2]+b[3]) + (b[0]+b[2]!=b[1]+b[3]) + (b[0]+b[3]!=b[1]+b[2])==3:
            k+=1
    print(k)
