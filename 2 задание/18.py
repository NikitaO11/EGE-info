print("x,y,w,z")
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if not(not((x==y) or (x==z)) or w or not(y<=z)):
                    print(x,y,w,z)