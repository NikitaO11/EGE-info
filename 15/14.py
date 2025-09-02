for a in range(-100,100):
    f = 1
    for x in range(100):
        for y in range(100):
            if ((y+2*x<a) or (x>20) or (y>30))==False:
                f=0
                break
    if f==1:
        print(a)
        break