print("x,y,w,z")
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(x and (y<=z) and ( (not(y)) <= ( (not(z)) == w ))):
                    print(x,y,w,z)
