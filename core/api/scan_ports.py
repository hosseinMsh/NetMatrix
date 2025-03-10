import socket

from core.api.utilities import DEFAULT_PORTS


def scan_ports(ip_address, start_port=None, end_port=None, use_default=True):
    if not ip_address:
        print("Usage: scan_ports(<IP_ADDRESS>, start_port=<START_PORT>, end_port=<END_PORT>, use_default=<True/False>)")
        return

    ports = []

    if start_port is not None and end_port is not None:
        ports = list(range(start_port, end_port + 1))
        print(f"Scanning ports {start_port} to {end_port} on {ip_address}...")
    elif use_default:
        ports = DEFAULT_PORTS
        print(f"Scanning important ports on {ip_address}...")
    else:
        print("No valid ports specified for scanning.")
        return

    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # تنظیم تایم‌اوت 1 ثانیه
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")


# مثال استفاده
scan_ports("81.31.170.182", start_port=20, end_port=25)
scan_ports("81.31.170.182")
