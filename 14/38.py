for a in range(1,100000):
    for x in range(14):
        for y in range(14):
            M = 2*15**5+y*15**4+2*15**3+3*15**2+x*15+5
            N = 6*13**4+7*13**3+x*13**2+9*13+y
            if (M+a)%N==0:
                print(a)

