```
# ARP Sniffer

## Introduction
ARP Sniffer is a Python script that allows users to discover IP and MAC addresses within a local network using ARP (Address Resolution Protocol) broadcasting.

## Features
- Discovers IP and MAC addresses within a local network.
- Allows users to specify IP and MAC addresses to be discovered.
- Customizable timeout duration for ARP requests.

## Requirements
- Python 3.x
- Scapy library (install via `pip install scapy`)

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/arp-sniffer.git
   ```
2. Navigate to the project directory:
   ```
   cd arp-sniffer
   ```
3. Run the script:
   ```
   python arp_sniffer.py -i <IP_ADDRESS> -m <MAC_ADDRESS> -t <TIMEOUT>
   ```
   Replace `<IP_ADDRESS>` with the target IP address, `<MAC_ADDRESS>` with the target MAC address, and `<TIMEOUT>` with the desired timeout duration (in seconds).

## Options
- `-i, --ipadress`: Specify the IP address to be discovered.
- `-m, --macadress`: Specify the MAC address to be discovered.
- `-t, --timeout`: Set the timeout duration for ARP requests (default is 1 second).

## Example
```
python arp_sniffer.py -i 192.168.1.1 -m 00:11:22:33:44:55 -t 2
```

## Acknowledgements
This script is inspired by the need for network analysis and security auditing. Special thanks to the Scapy library developers for their invaluable contribution.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Bu README dosyası, projenin ne yaptığını, nasıl kullanılacağını ve gerekli olanları anlatırken aynı zamanda özellikleri, gereksinimleri ve örnek kullanımı da sunmaktadır.
