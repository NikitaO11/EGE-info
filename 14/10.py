for x in "0123456789ABCDEFGHIJK":
    for y in "0123456789ABCDEFGHIJK":
        s = int("12"+y+x+"9",21)+int("36"+y+"99",21)
        if s%18==0:
            print((int("125"+x+"9",21)+int("36599",21))//18)
        break
