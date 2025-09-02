f = open("Дз2.txt").readline()
mt,t=0,0
for i in range(len(f)):
    if f[i]=="A" or f[i]=="B" or f[i]=="C":
        t+=1
        mt = max(mt,t)
    else:
        t=0
print(mt)