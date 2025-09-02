res=[]
for m in range(0,101,2):
    for n in range(1,101,2):
        t=2**m*5**n
        if 100000000<=t<=300000000:
            res.append([t,m+n])
print(sorted(res))
