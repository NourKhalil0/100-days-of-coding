#  Understanding DDoS Attacks

---

##  Overview

A DDoS (Distributed Denial of Service) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming it with a flood of internet traffic from multiple sources.


---

## What Is a DDos Attack?

- A DDoS attack uses multiple compromised systems (often part of a botnet) to flood a target with requests or data.
- The goal is to exhaust the target’s bandwidth, memory, or processing power, causing a crash or severe slowdowns.
- Its like feeding the server with too much "fake" requests, so the severer shuts down.

---

##  Common Types of DDoS Attacks

| Type      | Description                                                   |
|-----------|---------------------------------------------------------------|
| SYN Flood | Exploits TCP handshake by sending many incomplete requests    |
| UDP Flood | Overwhelms with UDP packets on random ports                   |
| HTTP Flood | Mimics legitimate user traffic at scale                       |
| ICMP (Ping) Flood | Sends massive ICMP Echo Requests (pings) to exhaust resources |
| Amplification | Exploits vulnerable servers to reflect large responses        |
| Slowloris | Opens many slow HTTp connections to tie up server threads     |

---

## Lab-Safe DDoS Simulation 

1. You can simulate basic traffic floods in a controlled lab environment using Python, Scapy, or tools like `hping3`, `slowloris`, or `LOIC` 
2. recommend using Scapy alot because, Scapy allows you to manipulate any data packet, which means that you can choose Whatever type you want to begin. 
3. Watch how easy its to domenstrate an actual DDOS attack:
>***Note***: This is Scapy running on terminal 
````bash
sudo scapy -c 'for i in range(1000): send(IP(src=RandIP(), dst="192.168.1.10")/TCP(sport=RandShort(), dport=80, flags="S"), verbose=0)'
````
---

## Input (From Attacker's Perspective):
1. Target IP or domain 
2. Type of flood (TCP/UDP/HTTP/ICMP)
3. Packet rate, size, concurrency

----

## Output (From Target's Perspective):
1. Extremely high traffic volume 
2. Resource exhaustion (RAM/CPU/Network)
3. Service crash or timeout 
4. Denial of access to legitimate users

---

#  DDoS Defense Techniques

## Network Level Mitigation
- Rate limiting
- Geo-blocking
- SYN cookies

## Application Level
- Captchas
- Load shedding
- Traffic scoring

## Infrastructure Level
- CDN services
- Cloud-based mitigation (e.g. Cloudflare, AWS Shield)

---

##  Legal Disclaimer⚠

> -This project is strictly for educational purposes .  
> -Dont perform DDoS attacks on any system you do not own or have explicit written permission to test.  
> -Unauthorized use is illegal and unethical.

---
### If you dont have Scapy, Run:
```bash
pip install scapy
```
# Run
``````bash
sudo python3 ddos_simulator.py
