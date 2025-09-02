for a in range(1,100):
    flag = True
    for x in range(1,100):
        for y in range(1,100):
            if (((y-x)!=10) or (a<x) or (a<y))==False:
                flag = False
                break
    if flag:
        print(a)