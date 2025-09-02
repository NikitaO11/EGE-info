from ipaddress import*
for mask in range(33):
    net1 = ip_network("112.117.107.70/"+str(mask),0)
    net2 = ip_network("112.117.121.80/"+str(mask),0)
    if net1.network_address==net2.network_address:
        print(net2.netmask)