f=open("9.txt")
k=0
for i in f:
    a=list(map(int,i.split()))
    a3=[x for x in a if a.count(x)==3]
    a1=[x for x in a if a.count(x)==1]
    if len(a3)==3 and len(a1)==3 and ((sum(a1))/3) > a3[1]:
        k+=1
        print(a,k)
