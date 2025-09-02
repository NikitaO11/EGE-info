f = open("24_7.txt")
s = f.readline()
while "QQ" in s:
    s = s.replace("QQ","Q Q")
s = s.split(" ")
print(len(max(s,key=len)))

mt,t=0,1
for i in range(len(s)-1):
    if s[i]=="Q" and s[i+1]=="Q":
        t=1
    else:
        t+=1
        mt = max(mt,t)
print(mt)