for a in range(100,-100,-1):
    flag = True
    for x in range(100,0,-1):
        for y in range(100,0,-1):
            if ((y-x>a) or (x+4*y>40) or (y-2*x<-35))==False:
                flag = False
                break
    if flag:
        print(a)