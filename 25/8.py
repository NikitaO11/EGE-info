for i in range(2,16):
    p = i*(i+1)*(i+2)*(i+3)
    for j in range(4,11):
        p=p*(i+j)
        if 100_000<=p<=400_000:
            print(p,i)
