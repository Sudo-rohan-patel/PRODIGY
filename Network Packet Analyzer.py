from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import datetime

# Function to process and display the captured packet details
def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Display packet details
        print(f"\n[{timestamp}] Packet captured:")
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")
        
        # Analyze TCP and UDP packets
        if packet.haslayer(TCP):
            print("TCP Packet")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
            print(f"Sequence Number: {packet[TCP].seq}")
        elif packet.haslayer(UDP):
            print("UDP Packet")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        
        # Display the payload (data) of the packet
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"Payload: {payload[:100]}...")  # Only show first 100 bytes of the payload

# Function to start sniffing packets
def start_sniffing(interface="eth0"):
    print(f"Starting packet capture on interface {interface}...")
    # Capture packets indefinitely until stopped (use Ctrl + C to stop)
    sniff(iface=interface, prn=packet_callback, store=0)

# Main entry point
if __name__ == "__main__":
    # Start sniffing on a specific network interface
    # On Windows, you may need to use a different interface (e.g., "Wi-Fi")
    interface = input("Enter the network interface to sniff on (e.g., 'eth0' or 'Wi-Fi'): ")
    start_sniffing(interface)
