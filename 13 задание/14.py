from ipaddress import*
for mask in range(33):
    net = ip_network("98.162.71.94/"+str(mask),0)
    if net.network_address == ip_address("98.162.71.64"):
        print(net.netmask)
net2 = ip_network("98.162.71.94/255.255.255.224",0)
print(net2.num_addresses-2)
