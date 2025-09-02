for x in "0123456789ABCDEFGHIJKL":
    for y in "0123456789ABC":
        s = int(x+"23"+x+"5",22)-int("67"+y+"9"+y,13)
        if abs(s)%57==0:
            print(x,y,s//57)
