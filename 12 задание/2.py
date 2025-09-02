s="4" + "1" * 92 + "4"
while ("13" in s) or ("114" in s) or ("1115" in s):
    if "13" in s:
        s=s.replace("13","4",1)
    elif "114" in s:
        s=s.replace("114","5",1)
    elif "1115" in s:
        s=s.replace("1115","3",1)
print(s)
