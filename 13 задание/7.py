from ipaddress import*
for mask in range(33):
    net = ip_network("98.162.75.91/"+str(mask),0)
    if net.network_address == ip_address("98.162.75.64"):
        print(net.netmask)
net = ip_network("98.162.75.91/255.255.255.224",0)
print(net.num_addresses)