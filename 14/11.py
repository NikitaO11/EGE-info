for x in "0123456789ABC":
    s = int("186"+x+"4",13)+int("5"+x+"716",13)
    if s%11==0:
        print(s//11)