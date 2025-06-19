# Scapy TCP 3-Way Handshake + HTTP GET Script
![](https://upload.wikimedia.org/wikipedia/commons/f/f0/Three-way-handshake-example.gif?20130203155226)
## Description

This project demonstrates how to manually establish a TCP connection with a target (IP address or DNS hostname) using Scapy, a powerful Python library for packet crafting and network analysis. After successfully completing the TCP 3 way handshake, the script sends a basic HTTP GET request and displays the server's response.

---

## Functionality

The script performs the following steps:

1. **User Input**:
   - The user is prompted to enter the destination IP address or DNS hostname.
   - Example inputs such as `www.google.com` or `10.58.83.178` are provided for guidance.

2. **TCP 3-Way Handshake**:
   - A TCP SYN packet is crafted and sent to port 80 (HTTP) of the target.
   - If a SYNACK response is received from the target , the script sends an ACK packet to complete the handshake.

3. **HTTP GET Request**:
   - After the TCP connection is established, the script constructs and sends an HTTP GET request manually.
   - It uses the `PA` (Push Ack) TCP flags to signal data transfer and pushes the request through the connection.

4. **Response Handling**:
   - The script listens for a response from the server.
   - If a response is received, it is displayed in a detailed format using Scapy’s built in packet visualizer.

---

## Requirements

- **Python 3.x**
- **Scapy** library
> **Note**: ⚠️ This script uses raw packet crafting and sending. It may require administrative privileges
---
## ⚠️Disclaimer
This script sends low level TCP and HTTP packets to a user specified target. It is intended strictly for educational and authorized testing purposes only.

Do not use this script against systems or networks without explicit permission, doing so may violate laws or organizational policies.
---
## Input
````
Enter the IPv4/DNS you want to establish connection with: www.google.com
````
---
## Output
```
Trying to connect...
Begin emission
...
Finished sending 1 packets
*
Received 4 packets, got 1 answers, remaining 0 packets
.
Sent 1 packets.
Begin emission
.
Finished sending 1 packets
.*
Received 3 packets, got 1 answers, remaining 0 packets
0000 IP / TCP 10.58.83.178:33437 > 216.58.207.228:http PA / Raw ==> IP / TCP 216.58.207.228:http > 10.58.83.178:33437 RA
None
```
---
##  Minimal Example: HTTP GET Using Python Sockets

```python
import socket

# Target host and port
host = "example.com"
port = 80

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((host, port))

# Send HTTP GET request
http_get = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n".format(host)
sock.send(http_get.encode())

# Receive and print response
response = sock.recv(4096)
print(response.decode())

sock.close()
```
---
## Run
```bash
sudo python3 3way.py
```
---
To install Scapy, run:
```bash
pip install scapy
