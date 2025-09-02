print("x,y,w,z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f1 = (x==y) and (w<=z)
                f2 = (x<=y)<=(w==z)
                if f1 == True and f2 == True:
                    print(x,y,w,z)