res=[]
for m in range(1,50,2):
    for n in range(0, 50, 2):
        if 250_000_000<=2**m*3**n<=450_000_000:
            res.append(2**m*3**n)
print(sorted(res))