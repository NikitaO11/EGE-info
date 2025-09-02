for x in "0123456789ABCDE":
    s1 = "131"+x+"1"
    s2 = "13"+x+"3"
    s = int(s1,15)+int(s2,17)
    if s%11==0:
        print(s//11)
