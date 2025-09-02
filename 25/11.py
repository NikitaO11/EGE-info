for i in range(2,22):
    p = i*(i+1)*(i+2)
    for j in range(3,22):
        p=p*(i+j)
        if 100000<=p<=250000:
            print(p,i,i+j)