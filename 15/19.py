for a in range(300):
    f=1
    for x in range(300):
        if ((x&102!=0) <=((x&36==0)<=(x&a!=0)))==False:
            f=0
            break
    if f==1:
        print(a)
        break