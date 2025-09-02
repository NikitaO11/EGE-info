s = open("24_2_2.txt").readline()
mt,t=0,1
for i in range(len(s)-1):
    if s[i]=="0" and s[i+1]=="0":
        t=1
    else:
        t+=1
        mt = max(mt,t)
print(mt)

s = s.replace("00","0 0")
s = s.split()
print(len(max(s,key=len)))
