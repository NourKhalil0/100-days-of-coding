from socket import *
import time

def scan_port(ip, ports):
    open_ports = []
    for port in ports:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
                open_ports.append(port)
            s.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    return open_ports

start_time = time.time()
common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995]
scan_port("127.0.0.1", common_ports)
end_time = time.time()
print(f"Scan took {end_time - start_time:.2f} seconds")



