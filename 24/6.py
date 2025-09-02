f = open("24_6.txt")
s = f.readline()
mt,t,sr=0,1,s[0]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        t+=1
        sr += s[i+1]
        if t>mt:
            mt = t
            res = sr
    else:
        t=1
        sr = s[i+1]
print(mt,res[0])

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        t+=1
        if t>mt:
            mt = t
            res = s[i-t+2]
    else:
        t=1
print(mt,res[0])