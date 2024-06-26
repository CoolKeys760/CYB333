# Lookup Vendor for a list of MAC Addresses
#
# V1.1 - Project from CYB216 with additional notes
#
# random list of MAC Addresses can be found at https://macaddress.io/mac-address-generator
# (options format 00:10:FA:6E:38:4A, lowercase, 48 bit, Multicast, UAA, prefix random, registered only)
#
# oui.txt can be downloaded from https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries
# *!* downloads may be limited to one per day *!*
# Download the "MAC Address Block Large (MA-L)" text file
# https://standards-oui.ieee.org/oui/oui.txt

mac_vendors = {}
with open("./oui.txt", "r") as f:
    for line in f:
        if "(hex)" in line:
            parts = line.strip().split("(hex)")
            mac_prefix = parts[0].strip()
            vendor_name = parts[1].strip()
            mac_vendors[mac_prefix] = vendor_name

with open('./macs.txt') as mac_list:
    for mac_address in mac_list:
        mac_prefix = mac_address[:8].upper().replace(":", "-")
        vendor_name = mac_vendors.get(mac_prefix, "Unknown")
        print("Device:", mac_address, "Vendor Name:", vendor_name, '\n')
