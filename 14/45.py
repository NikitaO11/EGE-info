for x in "0123456789ABCDE":
    s = "123"+x+"5"
    s1 = "1"+x+"233"
    res = int(s,15)+int(s1,15)
    if res%14==0:
        a = res//14
        print(a)

