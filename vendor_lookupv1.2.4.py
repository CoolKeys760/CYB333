# names:  Shawn Jung, Nathan Kovach, Robert Orona, and Mark Sanchez
# date: June 29th, 2024
# assignment title: Course Project

import os
import time
import urllib.request

# Define the directory and file paths
directory = 'C:\\Users\\ROB2\\CYBB333\\Final Project'
urlstr = 'https://standards-oui.ieee.org/oui/oui.txt'  # URL of IEEE OUI listing
fname = os.path.join(directory, 'oui.txt')  # filename for oui listing


def download_oui_file():
    oui = urllib.request.urlopen(urlstr)
    with open(fname, 'wb') as fhand:
        size = 0
        while True:
            info = oui.read(100000)
            if len(info) < 1:
                break
            size = size + len(info)
            fhand.write(info)
    print('Success!', size, 'characters copied to', fname, '\n')


print('\nChecking for updates to Organizationally Unique Identifier (OUI) Listing (oui.txt).....\n')

if os.path.exists(fname):  # Check if oui.txt exists locally
    urldt = dict(urllib.request.urlopen(urlstr).getheaders())['Last-Modified']  # date modified from URL
    filedt = time.strftime('%a, %d %b %Y', time.localtime(os.path.getctime(fname)))  # oui.txt date created
    print('     Local oui.txt created: ', filedt)
    print('     Latest from ieee.org:  ', urldt, '\n')
    if input('Update local ' + fname + ' (Y/n)?').strip().lower() == 'y':  # prompt to overwrite local file
        print('\nUpdating', fname)
        download_oui_file()
    else:
        print('\nLocal OUI data not updated. Utilizing oui.txt dated: ', filedt, '\n')
else:
    print(f'{fname} does not exist locally. Downloading...')
    download_oui_file()

input('Press Enter to continue.')

macs_file = os.path.join(directory, 'macs.txt')
if not os.path.exists(macs_file):
    print(f'Error: {macs_file} file not found. Please ensure the file exists in the specified directory.')
    exit(1)

mac_vendors = {}
with open(fname, "r", encoding="utf-8") as f:
    for line in f:
        if "(hex)" in line:
            parts = line.strip().split("(hex)")
            mac_prefix = parts[0].strip()
            vendor_name = parts[1].strip()
            mac_vendors[mac_prefix] = vendor_name

print('\nResults:\n')

results_file = os.path.join(directory, 'results.txt')
with open(macs_file, 'r', encoding="utf-8") as mac_list, open(results_file, 'w', encoding="utf-8") as result_file:
    for mac_address in mac_list:
        mac_prefix = mac_address[:8].upper().replace(":", "-")
        vendor_name = mac_vendors.get(mac_prefix, "Unknown")
        result = f"Device: {mac_address.strip()} Vendor Name: {vendor_name}"
        print(result)
        result_file.write(result + '\n')
