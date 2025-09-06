# Network_Scanner
A lightweight Python tool to scan local networks and discover active devices by their IP and MAC addresses. Built with `scapy`, this project is perfect for learning networking basics, penetration testing, or network monitoring.

## Features
- **IP and MAC Detection**: Lists all active devices on a specified subnet.
- **Simple CLI**: Easy-to-use command-line interface.
- **Export Results**: Save scan results to a CSV file for further analysis.
- **Extensible**: Can be integrated with tools like `nmap` for OS detection or vulnerability scanning.

## Installation
1. **Prerequisites**: Python 3.x installed.
2. **Install Dependencies**:
   ```bash
   pip install scapy

## How It Works
ARP Packets: The script sends ARP requests to all IPs in the specified subnet.
Response Analysis: Captures responses to determine active devices.
Output: Displays or saves IP/MAC pairs in a user-friendly format.
## Ethical Note
Use this tool only on networks you own or have explicit permission to scan.
Unauthorized scanning may violate privacy laws (e.g., CFAA, GDPR).
