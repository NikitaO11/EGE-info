from string import ascii_uppercase
f = open("Дз9.txt").readline()
a = ascii_uppercase[:8]
b="123456789"
mt,t=0,0
for i in range(len(f)):
    if f[i] in a or f[i] in b:
        t+=1
        mt = max(mt,t)
    else:
        t=0
print(mt)