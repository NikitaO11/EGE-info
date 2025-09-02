from ipaddress import*
for m in range(31):
    net1 = ip_network("120.91.176.213/"+str(m),0)
    net2 = ip_network("120.91.174.205/"+str(m),0)
    if net1.network_address==net2.network_address:
        print(m)