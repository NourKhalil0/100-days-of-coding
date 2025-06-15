import time
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
from scapy.all import IP, TCP, sr1, send

log = Lock()

def scan_port(ip, port, scan_type="s"):

    if scan_type == "s":
        flags = "S"
    elif scan_type == "n":
        flags = ""
    elif scan_type == "f":
        flags = "F"
    elif scan_type == "x":
        flags = "FPU"
    else:
        print("Ugyldig skannetype.")
        return

    pkt = IP(dst=ip) / TCP(dport=port, flags=flags)
    response = sr1(pkt, timeout=2, verbose=0)

    with log:
        with open("log.txt", "a") as f:
            if response:
                if response.haslayer(TCP):
                    flag = response[TCP].flags

                    if flag == 0x14:  # RST+ACK (lukket)
                        print(f"[CLOSED] Port {port}")
                        f.write(f"Port {port} is CLOSED\n")

                    elif flag == 0x12 and flags == "S":  # SYN+ACK (åpen for SYN-scan)
                        print(f"[OPEN]   Port {port}")
                        f.write(f"Port {port} is OPEN\n")
                        # Send RST for å lukke SYN-forbindelsen
                        rst = IP(dst=ip) / TCP(dport=port, flags="R")
                        send(rst, verbose=0)

                    else:
                        print(f"[UNDETERMINED] Port {port}, flag={flag}")
                        f.write(f"Port {port} returned flag {flag}\n")
                else:
                    print(f"[FILTERED] Port {port} (no TCP layer)")
                    f.write(f"Port {port} likely FILTERED\n")
            else:
                print(f"[NO RESPONSE] Port {port}")
                f.write(f"No response from port {port}\n")


def main():
    ip = input("Enter target IP address: ").strip()
    scan_type = input("Scan type: SYN (s), NULL (n), FIN (f), XMAS (x): ").lower()

    mode = input("Scan by range (r) or list (l)? ").lower()

    ports = []
    if mode == "r":
        try:
            start_port = int(input("Start port (min 20): "))
            end_port = int(input("End port (max 1000): "))
            if not (20 <= start_port <= end_port <= 1000):
                print("Invalid port range.")
                return
            ports = list(range(start_port, end_port + 1))
        except ValueError:
            print("Ports must be integers.")
            return

    elif mode == "l":
        port_input = input("Enter ports separated by commas (e.g. 22,80,443): ")
        try:
            ports = [int(p.strip()) for p in port_input.split(",") if p.strip().isdigit()]
        except ValueError:
            print("Invalid port list.")
            return
    else:
        print("Invalid scan mode.")
        return

    print(f"Scanning {len(ports)} ports on {ip} using {scan_type.upper()} scan...")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port, scan_type) for port in ports]
        for future in as_completed(futures):
            pass

    elapsed = time.time() - start_time
    print(f"Scan completed in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()
