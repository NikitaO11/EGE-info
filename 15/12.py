for a in range(1,100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((y+3*x<a) or (2*y+x>50) or (4*y-x)<40) ==False:
                flag = False
                break
    if flag:
        print(a)
        break