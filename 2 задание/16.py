print("x,y,w,z")
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if not(((x and y)<=(not(z))) and (x<=y) or w):
                    print(x,y,w,z)