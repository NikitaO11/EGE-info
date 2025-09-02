f = open("24re_8.txt").readline()
f = f.replace("A"," ")
f = f.split(" ")
res=[]
for i in f:
    if i.count("B")>=3:
        res.append(i)
print(len(max(res,key=len)))