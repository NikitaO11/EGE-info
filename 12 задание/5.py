for i in range(2,50):
    s="4" * i
    while "222" in s or "444" in s:
        s=s.replace("222","4",1)
        s = s.replace("444", "22", 1)
    print(s)