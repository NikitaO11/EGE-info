f = open("17-18.txt")
s=[int(x) for x in f]
res=[]
ch = [x for x in s if x%2==0]
a = sum(ch)/len(ch)
print(a)
for i in range(len(s)-1):
    if (s[i]%3==0) or (s[i+1]%3==0):
        if s[i]<a or s[i+1]<a:
            sum = s[i]+s[i+1]
            res.append(sum)
print(len(res),max(res))