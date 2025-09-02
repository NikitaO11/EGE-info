from ipaddress import*
for mask in range(31):
    net1=ip_network("118.187.59.255/"+str(mask),0)
    net2=ip_network("118.187.65.115/" + str(mask), 0)
    if net1.network_address!=net2.network_address :
        print(mask)


