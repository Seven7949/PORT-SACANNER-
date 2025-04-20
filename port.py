import socket
from datetime import datetime

def scan_ports(target, ports):
    print(f"🔍 Scanning {target} for open ports...\n")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    s.send(b'WhoAreYou\r\n')
                    banner = s.recv(1024).decode().strip()
                    print(f"[OPEN] Port {port} - Banner: {banner}")
                except:
                    print(f"[OPEN] Port {port} - Banner not available")
            s.close()
        except socket.error:
            print(f"❌ Could not connect to {target}:{port}")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    port_range = input("Enter port range (e.g., 20-100): ")

    try:
        start, end = map(int, port_range.split('-'))
        ports = list(range(start, end + 1))
        start_time = datetime.now()
        scan_ports(target, ports)
        duration = datetime.now() - start_time
        print(f"\n⏱️ Scan completed in {duration}")
    except ValueError:
        print("Invalid input. Use format like 20-80.")
