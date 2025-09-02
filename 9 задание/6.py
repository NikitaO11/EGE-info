f = open("9-6.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    a1 = [x for x in a if a.count(x)==2]
    a2 = [x for x in a if a.count(x)==1]
    if len(a1)==4 and len(a2)==2:
        if sum(set(a1))>sum(a2):
            k+=1
print(k)