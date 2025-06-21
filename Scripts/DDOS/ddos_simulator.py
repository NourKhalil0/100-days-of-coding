from scapy.all import *
from scapy.layers.inet import IP, TCP

target = "127.0.0.1"
port = 80

for i in range(100):
    IP_pkt = IP(dst=target)
    TCP_pkt = TCP(dport=port, flags="S")
    print(f"{i} SYN sent\n")

    send(IP_pkt/TCP_pkt, verbose=0)

print(f"RESULTS: "
      f"{i} SYN packets sent")
