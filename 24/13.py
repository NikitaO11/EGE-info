s = open("24_2_3.txt").readline()
mt,t=0,0
for i in range(len(s)-1):
    if s[i]=="Q" and s[i+1]=="Q":
        t=1
    else:
        t+=1
        mt = max(mt,t)
print(mt)

s = s.replace("QQ","Q Q")
s = s.split()
print(len(max(s,key=len)))