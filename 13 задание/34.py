from ipaddress import*
net = ip_network("158.129.45.123/255.255.0.0",0)
k=0
for ad in net:
    a = bin(int(ad))[2:]
    l = a[0:16]
    r = a[16:32]
    if r.count("1")/l.count("1")>2:
        k+=1
print(k)