from scapy.all import ARP, Ether, srp
import argparse
import csv
def network_scanner(target_ip):
                                                # Create ARP packet
    arp = ARP(pdst=target_ip)
    # Create Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
                                                # Combine the frames
    packet = ether/arp
    # Send the packet and capture responses
    result = srp(packet, timeout=3, verbose=0)[0]
                                                # Parse the responses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def display_results(devices):
    print("Available devices in the network:")
    print("IP" + " " * 18 + "MAC")
    for device in devices:
        print(f"{device['ip']:20} {device['mac']}")
                                             # Export Results to a File

def save_to_csv(devices, filename="network_devices.csv"):
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "MAC"])
        for device in devices:
            writer.writerow([device['ip'], device['mac']])
    print(f"Results saved to {filename}")


if __name__ == "__main__":
    target_ip = "192.168.1.1/24"  
    devices = network_scanner(target_ip)
    display_results(devices)
