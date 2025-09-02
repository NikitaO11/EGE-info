s="3"*247
while ("444" in s) or ("333" in s):
    if "444" in s:
        s=s.replace("444","3",1)
    else:
        s=s.replace("333","4",1)
print(s)