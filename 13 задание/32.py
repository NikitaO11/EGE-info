from ipaddress import*
k=0
net = ip_network("157.180.63.114/255.255.255.248",0)
for ad in net:
    a = bin(int(ad))[2:]
    l = a[0:16]
    r = a[16:32]
    if l.count("1")>=r.count("1"):
        k+=1
print(k)