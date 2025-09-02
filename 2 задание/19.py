print("x,y,w,z")
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if not(y and (x<=w) and ((not(x)) <= ((not(w))==z))):
                    print(x,y,w,z)