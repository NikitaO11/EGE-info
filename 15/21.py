for a in range(-100,100):
    f=1
    for x in range(0,100):
        for y in range(0,100):
            if ((x>=20) or (y>=40) or (y<=x+a) or (y>=3*x-a))==0:
                f=0
                break
    if f==1:
        print(a)
