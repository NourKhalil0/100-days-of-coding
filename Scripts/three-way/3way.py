from scapy.all import *
from scapy.layers.inet import IP, TCP

get = 'GET / HTTP/1.0\r\n\r\n'

ip = input("Enter the IPv4/DNS you want to establish connection with: ")
print("Example DNS: www.google.com")
print("Example IP: 10.58.83.178")
port = RandNum(1024, 65535)

print("Trying to connect...")
syn = IP(dst=ip)/TCP(sport=port, dport=80, flags="S", seq=42)
synAck = sr1(syn, timeout=2)

if synAck and synAck.haslayer(TCP) and synAck.getlayer(TCP).flags == "SA":

    ack = IP(dst=ip)/TCP(sport=port, dport=80, flags="A",
                         seq=synAck.ack, ack=synAck.seq + 1)
    send(ack)

    http_get = IP(dst=ip)/TCP(sport=port, dport=80, flags="PA",
                              seq=synAck.ack, ack=synAck.seq + 1)/get
    reply, error = sr(http_get, timeout=2)

    print(reply.show())
else:
    print("No SYN ACK received, connection failed.")
