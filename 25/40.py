def deln(n):
    res=[]
    flag = False
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            flag = True
            res.append(i)
            if n//i!=i:
                res.append(n//i)
    if flag == False:
        return 0
    else:
        return res


for x in range(501201,525000):
    if deln(x)!=0:
        r = sum(deln(x))
        if r%10==3:
            print(x,r)
