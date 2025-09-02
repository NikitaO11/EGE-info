print("x,y,w,z")
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((w<=y)<=x) or not(z)):
                    print(x,y,w,z)
