res=[]
for n in range(1000):
    n2 = bin(n)[2:]
    if n%2==0:
        n2 = n2+"10"
    else:
        n2 = "1"+n2+"10"
    r = int(n2,2)
    if r<=110:
        res.append(r)
print(max(res))