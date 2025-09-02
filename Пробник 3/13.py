from ipaddress import*
net = ip_network("142.29.122.138/255.255.192.0",0)
for ad in net:
    print(ad)