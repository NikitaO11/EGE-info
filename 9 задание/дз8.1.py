f = open("дз8.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    a1 = [x for x in a if a.count(x)>=2]
    a2 = [x for x in a if a.count(x)==1]
    if len(a1)>=2 and len(a2)>=1:
        if (sum(a1)/len(a1))>(sum(a2)/len(a2)):
            k+=1
print(k)