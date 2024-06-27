import nmap

def scan_network(ip_range):
    nm = nmap.PortScanner()
    
    # Scan the specified IP range
    nm.scan(hosts=ip_range, arguments='-sP')
    
    mac_addresses = []
    
    # All hosts found
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            mac_address = nm[host]['addresses']['mac']
            mac_addresses.append(mac_address)
    
    return mac_addresses

# Specify the IP range 
ip_range = '192.168.1.0/24'

# scan_network function
mac_addresses = scan_network(ip_range)

# Print found MAC addresses
print("Found MAC Addresses:")
for mac in mac_addresses:
    print(mac)
