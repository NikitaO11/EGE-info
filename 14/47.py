for x in "0123456789ABCDEF":
    s1 = "1"+x+"BAD"
    s2 = "2C"+x+"FE"
    s = int(s1,16)+int(s2,16)
    if s%15==0:
        print(s//15)