from ipaddress import*
net = ip_network("211.67.112.134/255.255.255.192",0)
k=0
for ad in net:
    a = bin(int(ad))[2:]
    l = a[0:16]
    r = a[16:32]
    if l.count("1")>=r.count("1"):
        k+=1
print(k)