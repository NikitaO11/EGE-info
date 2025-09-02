for a in range(1,100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((x+4*x!=120) or (x>a) or (y>a))==False:
                flag = False
                break
    if flag:
        print(a)