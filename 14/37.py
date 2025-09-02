for p in range(9,37):
    for x in range(1,p+1):
        for y in range(1,p+1):
            t1 = 3*p**3+4*p**2+x*p+5
            t2 = x*p**3+9*p**2+x*p+3
            t3 = y*p**3+y*p**2+6*p+8
            if t1+t2==t3:
                print(y*p**3+x*p**2+x*p+y)
