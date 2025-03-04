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


def ping_target(target, packet_count=4, verbose=True):
    """
    Pings a target (domain or IP) using the system ping command,
    extracts the average ping time, and prints messages if verbose is True.

    Parameters:
        target (str): The domain or IP to ping.
        packet_count (int): Number of ping packets to send.
        verbose (bool): If True, prints the ping output messages.

    Returns:
        str or None: The average ping time as a string (e.g. "23") if successful, otherwise None.
    """
    os_type = platform.system().lower()
    # Define regex patterns for Windows and Unix-like systems.
    regex_pattern = (
        r"Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms"
        if os_type == "windows"
        else r"min/avg/max/mdev = ([\d.]+)/([\d.]+)/([\d.]+)"
    )

    if verbose:
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
            if verbose:
                print(f"Error: {target} is not reachable.")
            return None

        # Extract the average ping time.
        match = re.search(regex_pattern, output)
        if match:
            avg_ping = match.group(3) if os_type == "windows" else match.group(2)
            if verbose:
                print(f"Success: {target} is reachable. Average ping: {avg_ping} ms")
            return avg_ping
        else:
            if verbose:
                print(f"Error: Could not extract ping statistics for {target}.")
            return None

    except subprocess.TimeoutExpired:
        if verbose:
            print(f"Error: Ping timed out for {target}.")
    except Exception as e:
        if verbose:
            print(f"Error: Failed to ping {target} - {e}")
    return None


def ping_all_addresses(domain, packet_count=4, port=443, print_domains_flag=False, print_ping_flag=True):
    """
    Retrieves all domains (from the certificate's SAN extension) associated with the given domain,
    pings each one, and returns a mapping of domain to its average ping time.

    Parameters:
        domain (str): The target domain.
        packet_count (int): Number of ping packets to send.
        port (int): The port to use for SSL certificate extraction.
        print_domains_flag (bool): If True, prints the resolved domains.
        print_ping_flag (bool): If True, prints the ping output for each target.

    Returns:
        dict: A mapping of each domain to its ping result (None if unreachable or on error).
    """
    domains = resolve_all_domains(domain, port)
    mapping = {}

    if print_domains_flag:
        print(f"\nResolved {domain} to the following domains from its certificate:")
        for d in domains:
            print(f"  - {d}")

    for d in domains:
        result = ping_target(d, packet_count, verbose=print_ping_flag)
        mapping[d] = result

    return mapping


if __name__ == "__main__":
    domain = "sharif.ir"  # Change to your target domain
    result_mapping = ping_all_addresses(domain, print_domains_flag=True, print_ping_flag=True)
    print("\nMapping of <domain, ping> results:")
    for d, ping_val in result_mapping.items():
        print(f"{d}: {ping_val}")
