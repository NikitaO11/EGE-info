def f(n):
    res=[]
    flag = False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            flag = True
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    if flag == False:
        return 0
    else:
        return res

for n in range(700001,710000+1):
    if f(n)!=0:
        m = min(f(n))+max(f(n))
        if m%10==4:
            print(n,m)
