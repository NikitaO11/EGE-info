s = open("24_09.txt").readline()
mt,t=0,1
for i in range(len(s)-1):
    if s[i]<=s[i+1]:
        t+=1
        mt = max(mt,t)
    else:
        t=1
print(mt)
