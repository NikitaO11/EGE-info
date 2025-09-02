for a in range(-100,300):
    f = 1
    for x in range(100):
        for y in range(100):
            if ((y+4*x<a) or (x+4*y>120) or (5*x-2*y>50))==False:
                f = 0
                break
    if f==1:
        print(a)
        break