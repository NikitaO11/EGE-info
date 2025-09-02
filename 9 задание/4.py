f = open("9-4.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    a1=[x for x in a if a.count(x)==1]
    if a[3] > a[0]+a[1]+a[2]:
        if len(a1)==4:
            k+=1
    print(k)
# f = open("9-4.txt")
# k=0
# for i in f:
#     a = sorted(list(map(int,i.split())))
#     if a[3] > a[0]+a[1]+a[2]:
#         if a[0]!=a[1]!=a[2]!=a[3]:
#             k+=1
#     print(k)