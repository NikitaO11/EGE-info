def delp(n):
    res=[]
    flag=False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            res.append(i)
            flag=True
    if flag==True:
        return res
    else:
        return 0

for n in range(850000,2000000):
    m = delp(n)
    if m!=0:
        result=m[-1]-m[0]
        if result%5==0:
            print(n,result)
