from ipaddress import*
net = ip_network("1.1.1.1/255.255.255.224",0)
print(net.num_addresses-2)