from scapy.all import *
from collections import defaultdict
from scapy.layers.inet import TCP, IP

syn_count = defaultdict(int)
def detect_scan(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].flags == 'S':
        src = pkt[IP].src
        dst = pkt[IP].dst
        syn_count[src] += 1
        print(f"SYN from {src} to port {dst} (Total: {syn_count[src]})")

        if syn_count[src] >= 20:
            print("Possible scan detected")

print("Sniffing...")
sniff(filter="tcp", prn=detect_scan, store=0)

