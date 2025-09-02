for n in range(4,10000):
    s="4" + "8" * n
    while "48" in s or "288" in s or "8888" in s:
        if "48" in s:
            s=s.replace("48","8",1)
        if "288" in s:
            s=s.replace("288","84",1)
        if "8888" in s:
            s=s.replace("8888","2",1)
    sum = 2*s.count("2") + 4*s.count("4") + 8*s.count("8")
    if sum == 56:
        print(n)
        break


