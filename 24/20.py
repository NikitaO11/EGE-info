s = open("24_2_10.txt").readline()
mt,t=0,0
for i in range(len(s)):
    if s[i] in "0123456789ABCDEFGH":
        t+=1
        mt = max(mt,t)
    else:
        t=0
print(mt)
