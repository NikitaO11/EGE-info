for n in range(4,10000):
    s="6" + "9" * n
    while "69" in s or "399" in s or "9999" in s:
        if "69" in s:
            s=s.replace("69","9",1)
        if "399" in s:
            s = s.replace("399", "96", 1)
        if "9999" in s:
            s = s.replace("9999", "3", 1)
    sum1 = 3*s.count("3") + 6*s.count("6") + 9*s.count("9")
    if sum1 ==54:
        print(n)
        break
    # sum2=sum(map(int,s))
    # if sum2==54:
    #     print(n)
    #     break
