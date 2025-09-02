f = open("дз2.txt")
k=0
for line in f:
    a = list(map(int,line.split()))
    flag = False
    for i in range(4):
        for j in range(i+1,4):
            for q in range(j+1,4):
                if (a[i]+a[j]+a[q])%2!=0:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        k+=1
print(k)