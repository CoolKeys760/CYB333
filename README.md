This python tool is for our CYB333 course project.

The purpose of the script is to automate identification of the hardware vendors for all devices on a network from a text file.
  macs.txt is a list of all the MAC address you want to lookup.  This can be generated from a netowrk scan, arp -an, router listing, etc..
  example format for mac addresses is B8:4C:87:D2:58:34

Vendors are identified by thier Organizationally Unique Identifier (OUI)
  Latest oui.txt can be downloaded from https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries
  Download the "MAC Address Block Large (MA-L)" text file 
  direct link: https://standards-oui.ieee.org/oui/oui.txt

Sample oui.txt and mac.txt files are provided for testing.

Random list of MAC Addresses generated at https://macaddress.io/mac-address-generator
(options format 00:10:FA:6E:38:4A, lowercase, 48 bit, Multicast, UAA, prefix random, registered only)
