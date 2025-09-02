
for n in range(9999,4,-1):
    s="2" + "8" * n
    while "28" in s or "388" in s or "888" in s:
        if "28" in s:
            s=s.replace("28","8",1)
        if "388" in s:
            s=s.replace("388","82",1)
        if "888" in s:
            s=s.replace("888","3",1)
    sum = 2*s.count("2")+3*s.count("3") + 8*s.count("8")
    if s.count("8") == 2:
        print(n)
        break