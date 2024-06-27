# MAC Address Vendor Lookup

This project is designed to look up the vendor information for a list of MAC addresses. It includes functionality to check for and download the latest OUI (Organizationally Unique Identifier) list from the IEEE website.

## Version History

- **V1.1** - Project from CYB333 with additional notes
- **V1.2** - Added check online for updated oui.txt from ieee.org and option to download
- **V1.3** - Added functionality to save the results to a file (`results.txt`)
- **V1.4** - Improved error handling to ensure `oui.txt` is downloaded if it does not exist
- **V1.5** - Added encoding handling to prevent `UnicodeDecodeError` when reading `oui.txt`
- **V1.6** - Added check to ensure `macs.txt` exists before processing

## Usage

1. Run the script to check for updates to the OUI list and optionally download the latest version.
2. Ensure that `macs.txt` is present in the specified directory (`C:\Users\ROB2\CYBB333\Final Project`). The file should contain the list of MAC addresses to look up.
    - Create `macs.txt` with the following format:
        ```
        00:1A:2B:3C:4D:5E
        00:1B:2C:3D:4E:5F
        00:1C:2D:3E:4F:5G
        ```
3. The script will read the `macs.txt` file for MAC addresses and output the vendor names.
4. Results will be displayed on the console and saved to a file named `results.txt` in the same directory.

## Requirements

- Python 3.x
- Internet connection to download the OUI list

## Files

- `oui.txt`: The local copy of the OUI list.
- `macs.txt`: A file containing the list of MAC addresses to look up.
- `results.txt`: A file where the lookup results will be saved.

## Running the Script

```bash
python C:\Users\ROB2\CYBB333\Final Project\vendor_lookupv1.2.py
