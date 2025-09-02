from ipaddress import*
k=0
net = ip_network("106.184.0.0/255.248.0.0",0)
for ad in net:
    ed = bin(int(ad))[2:].count("1")
    if ed%2!=0:
        k+=1
print(k)
