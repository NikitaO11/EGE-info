def delp(n):
    res=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    return res
for n in range(3954,8979+1):
    sp = delp(n)
    if 41<=len(sp)<=45:
        print(n,len(sp))