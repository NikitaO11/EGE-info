f = open("17-17.txt")
s = [int(x) for x in f]
res=[]
for i in range(len(s)-1):
    if abs(s[i])%5==0 and abs(s[i+1])%5==0:
        sum = s[i]+s[i+1]
        res.append(sum)
print(len(res),max(res))