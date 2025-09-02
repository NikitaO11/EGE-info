for a in range(1,100):
    flag = True
    for x in range(1,100):
        for y in range(1,100):
            if ((y+2*x!=99) or (y>a) or (x>a)) == False:
                flag = False
                break
    if flag:
        print(a)