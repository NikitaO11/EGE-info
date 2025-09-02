from string import ascii_uppercase
from string import*
s = open("24-1.txt").readline()
st = ""
for i in range(len(s)-1):
    if s[i]=="X":
        st+=s[i+1]
alf = ascii_uppercase
mx = 0
for x in alf:
    if st.count(x)>mx:
        mx = st.count(x)
        sym=x
print(sym,st.count(sym))