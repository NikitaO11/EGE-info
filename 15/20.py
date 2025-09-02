for a in range(300):
    f=1
    for x in range(300):
        if ((x&85==0)<=((x&54!=0)<=(x&a!=0)))==False:
            f=0
            break
    if f==1:
        print(a)
        break