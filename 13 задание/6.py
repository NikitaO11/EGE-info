from ipaddress import*
net = ip_network("145.205.76.0/255.255.192.0",0)
k=0
for ad in net:
    ed = bin(int(ad))[2:].zfill(32).count("0")
    if ed%2!=0:
        k+=1
        print(k)