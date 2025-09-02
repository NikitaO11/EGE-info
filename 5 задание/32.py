res=[]
for n in range(100):
    n2 = bin(n)[2:]
    if n%2==0:
        n2 = "1"+n2+"0"
    else:
        n2 = "11" + n2 + "11"
    r=int(n2,2)
    if r>225:
        res.append(r)
print(min(res))
