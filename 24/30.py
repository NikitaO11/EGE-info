f = open("24_досрок.txt").readline()
ts=""
maxt=0
for x in f:
    if x not in "0123456789AB":
        ts=""
    else:
        ts+=x
        tch = int(ts,12)
        if tch%2==0 and len(ts)>maxt and ts[0]!="0":
            maxt = len(ts)
print(maxt)

