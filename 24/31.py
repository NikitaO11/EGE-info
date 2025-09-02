f = open("24re_1.txt").readline()
mt,t=0,0
for i in range(len(f)):
    if f[i]=="C":
        t+=1
        mt = max(t,mt)
    else:
        t=0
print(mt)