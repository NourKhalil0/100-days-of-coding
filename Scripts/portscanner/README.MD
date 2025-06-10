## Port Scanner
A simple and efficient Python port scanner that checks for open ports on a specified IP address.
--- 

## Features

1. Fast TCP port scanning
2. Configurable timeout settings
3. Error handling for failed connections
4. Performance timing
5. Customizable port lists

---

## Requirements

1. Python 3.x
2. No external dependencies (uses built-in libraries)

---

## Installation

Clone this repository:
```bash 
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
````
---

## Run the script:
```bash
  python3 port_scanner.py
```
---

## Example input
```python
common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995]
scan_port("127.0.0.1", common_ports)
```
---

## Example output

```python
Port 22 is open
Port 80 is open
Port 443 is open
Scan took 2.34 seconds
```
---
## Configuration
You can modify the timeout setting by changing the
```sql
s.settimeout(1) value:

Lower values = faster scanning, may miss slower services
Higher values = more thorough, but slower scanning
```
---
## Important Notes
![](https://raw.githubusercontent.com/NourKhalil0/100-days-of-coding/main/images/_Pngtree_black_exclamation_mark_warning_sign_5489468-removebg-preview.png)

1. ⚠️ Legal Notice: Only use this tool on networks and systems you own or have explicit permission to test. Unauthorized port scanning may be illegal in your jurisdiction.
2. ⚠️ Ethical Use: This tool is intended for legitimate security testing, network diagnostics, and educational purposes only.
