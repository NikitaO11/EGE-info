s= "3" * 45 + "0" *45 + "2" * 45
while "02" in s or "32" in s or "30" in s:
    if "02" in s:
        s=s.replace("02","20",1)
    if "32" in s:
        s=s.replace("32","23",1)
    if "30" in s:
        s = s.replace("30", "03", 1)
print(s[14],s[74],s[114])