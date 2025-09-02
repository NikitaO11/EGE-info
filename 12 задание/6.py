min1=10**6
for i in range(102,300):
    s="1" * i
    while "111" in s:
        s=s.replace("111","99",1)
        s = s.replace("999", "11", 1)
    if s.count("1") < min1:
        min1=s.count("1")
        dl=i
print(dl, min1)
