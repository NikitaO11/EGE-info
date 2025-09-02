for n in range(4,10000):
    s="5" + "1" * n
    while "71" in s or "511" in s or "1111" in s:
        if "71" in s:
            s=s.replace("71","1",1)
        if "511" in s:
            s=s.replace("511","17",1)
        if "1111" in s:
            s=s.replace("1111","5",1)
    sum=5*s.count("5")+7*s.count("7")+1*s.count("1")
    if sum>61:
        print(n)
        break