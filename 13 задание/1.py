from ipaddress import*
net = ip_network("217.16.246.2/255.255.252.0",0)
print(net.network_address)