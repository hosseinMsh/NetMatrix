import subprocess
import re
import platform
import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend

from core.api.get_san_domains import get_san_domains


def resolve_all_domains(domain, port=443):
    """
    Resolves all domains from the SSL certificate's SAN extension for the given domain.
    Removes duplicate entries while preserving order.
    """
    domains = get_san_domains(domain, port)
    # Remove duplicates while preserving order.
    return list(dict.fromkeys(domains))


def ping_target(target, packet_count=4):
    """
    Pings a target (domain or IP) using the system ping command,
    extracts and prints the average ping time.
    """
    os_type = platform.system().lower()
    # Define regex patterns for Windows and Unix-like systems.
    regex_pattern = (
        r"Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms"
        if os_type == "windows"
        else r"min/avg/max/mdev = ([\d.]+)/([\d.]+)/([\d.]+)"
    )

    print(f"\nPinging {target}...")
    command = ["ping", "-n" if os_type == "windows" else "-c", str(packet_count), target]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        output = result.stdout + result.stderr

        # Check for complete packet loss.
        if "100% packet loss" in output or re.search(r"100\.0% packet loss", output):
            print(f"Error: {target} is not reachable.")
            return None

        # Extract the average ping time.
        match = re.search(regex_pattern, output)
        if match:
            avg_ping = match.group(3) if os_type == "windows" else match.group(2)
            print(f"Success: {target} is reachable. Average ping: {avg_ping} ms")
            return avg_ping
        else:
            print(f"Error: Could not extract ping statistics for {target}.")
            return None

    except subprocess.TimeoutExpired:
        print(f"Error: Ping timed out for {target}.")
    except Exception as e:
        print(f"Error: Failed to ping {target} - {e}")
    return None


def ping_all_addresses(domain, packet_count=4, port=443):
    """
    Retrieves all domains (from the certificate's SAN extension) associated
    with the given domain and pings each one.
    """
    domains = resolve_all_domains(domain, port)

    print(f"\nResolved {domain} to the following domains from its certificate:")
    for d in domains:
        print(f"  - {d}")

    for d in domains:
        ping_target(d, packet_count)


if __name__ == "__main__":
    domain = "www.lichess.org"  # Change to your target domain
    ping_all_addresses(domain)
