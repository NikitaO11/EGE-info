f = open("24_2.txt")
s = f.readline()
mt,t=0,0
for i in range(len(s)):
    if s[i]!="Z":
        t+=1
        mt = max(mt,t)
    else:
        t=0
print(mt)
mmt=0
s = s.replace("Z"," ")
s = s.split(" ")
for x in s:
    mmt = max(mt,len(x))
print(mmt)