# TCP SYN Scan Detector with Scapy

This is a simple Python script using **Scapy** to detect potential TCP SYN-based port scans (like those performed with Nmap). It sniffs incoming traffic and flags suspicious IPs that send a high number of SYN packets in a short time.
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyv7uAFL5i1AK6YF0OqoPyUF6h9GfB8EYzig4-zM1Tz4I2H3mVTKggdK23R1rCGkqG5ZtnKAYUWGnyfJBQ2Xs8q0-CozpHxrHd83ptzZE37QOATobB___azUfDsqubbqfazDRkFc836bDo3OkykdanwMWB5K8QnQap9AyjplhDzq-YRBR1hes2BE8JHF8/s16000/SYN.webp)

## Features

- Detects SYN packets (used in port scans)
- Tracks and counts per-source IP
- Flags IPs sending 20 or more SYNs
- Real-time output in terminal
- Lightweight and fast
---
## Requirements

- Python 3.x
- Scapy
---
Install Scapy via pip if you don't already have it:

```bash
pip install scapy
```
---
## Run
````bash
sudo python3 scan_detector.py
````
---
## Output
You should see output like this:
````python
Sniffing...
SYN from 192.168.1.45 to port 192.168.1.10 (Total: 1)
SYN from 192.168.1.45 to port 192.168.1.10 (Total: 2)
...
⚠️ Possible scan detected
````
---
## How It Works
This script captures TCP packets and checks for SYN flags (flags='S'), which are typically the first step in a TCP connection (or a port scan). It then:
1. Extracts the source and destination IP from the packet.
2. Tracks the number of SYNs seen from each source IP.
3. Prints a warning if a source sends 20 or more SYNs
---
## ⚠️ Disclaimer
This script is for educational and defensive purposes only. Do not use it for malicious scanning or monitoring of unauthorized networks.

![](https://itexamanswers.net/wp-content/uploads/2020/11/Performing-Port-Scans.gif)