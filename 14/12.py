for x in "0123456789ABCDEF":
    s = int("1"+x+"BAD",16)+int("2C"+x+"FE",16)
    if s%15==0:
        print(s//15)