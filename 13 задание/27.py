from ipaddress import*
for mask in range(33):
    net = ip_network("48.95.137.38/"+str(mask),0)
    if ip_address("48.95.128.0") == net.network_address:
        print(mask)