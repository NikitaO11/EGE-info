from string import*
f = open("24-s1.txt")
minA=10*10
for s in f:
    kA=s.count("A")
    if kA<minA:
        minA=kA
        st=s
alf = ascii_uppercase
mx = 0
for x in alf:
    if st.count(x) >= mx:
        mx = st.count(x)
        sym = x
print(sym)

res=0
f = open("24-s1.txt")
for s in f:
    res+=s.count(sym)
print(res)