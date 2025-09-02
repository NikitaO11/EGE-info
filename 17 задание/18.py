f = open("17-1.txt")
s = [int(x) for x in f]
res=[]
maxs = max([x for x in s if x%3==0 ])
for i in range(len(s)-1):
    if (s[i]%3==0)+(s[i+1]%3==0)>=1:
        if (s[i]+s[i+1])<maxs:
            sum = s[i]+s[i+1]
            res.append(sum)
print(len(res),max(res))