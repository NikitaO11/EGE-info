for a in range(1000):
    f = 1
    for x in range(1000):
        if ((x&56!=0)<=((x&48==0)<=(x&a!=0)))==False:
            f=0
            break
    if f==1:
        print(a)
        break