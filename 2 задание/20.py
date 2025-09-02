print("x,y,w,z")
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f1 = (x or (not(y))) <= (w==z)
                f2 = (x or (not(y))) == (z<=w)
                if f1 == False and f2 == False:
                    print(x,y,w,z)