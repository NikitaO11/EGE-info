for x in "0123456789abcdefghijklm":
    x1 = "7"+x+"38596"
    x2 = "14"+x+"36"
    x3 = "61"+x+"7"
    res = int(x1,23)+int(x2,23)+int(x3,23)
    if res%22==0:
        print(res//22)
