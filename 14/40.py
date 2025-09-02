for x in range(0,10):
    p1 = int("123"+str(x)+"5")
    p2 = int("1" + str(x)+"233")
    t1 = 1*p1+5
    t2 = 1*p2+5
    if (t1+t2)%14==0:
        print((t1+t2)//14)
