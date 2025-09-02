f = open("Дз8.txt").readline()
mt,t=0,1
for i in range(len(f)-1):
    if f[i]<=f[i+1]:
        t+=1
        mt=max(mt,t)
    else:
        t=1
print(mt)

