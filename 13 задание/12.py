from ipaddress import*
net = ip_network("187.127.0.0/255.255.240.0",0)
k=0
for ad in net:
    ed = bin(int(ad))[2:].count("1")
    if ed%3==0:
        k+=1
print(k)