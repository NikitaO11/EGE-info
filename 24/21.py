s = open("24_3_12.txt").readline()
k=0
mt,t=0,1
for i in range(len(s)-1):
    if s[i] == ".":
        k+=1
    if s[i]!="." and k<=1:
        t+=1
        mt=max(mt,t)
    else:
        t=1
        k=0
print(mt)
