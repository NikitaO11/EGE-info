res=[]
for m in range(0,50,2):
    for n in range(1,50,2):
        if 200_000_000<=2**m*3**n<=400_000_000:
            res.append(2**m*3**n)
print(sorted(res))