from ipaddress import*
net = ip_network("172.16.168.0/255.255.248.0",0)
k=0
for ad in net:
    ed = bin(int(ad))[2:].zfill(32).count('1')
    if ed%5!=0:
        k+=1
print(k)