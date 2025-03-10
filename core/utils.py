import ssl
import socket
import requests
from datetime import datetime
import whois

def check_ssl_expiration(domain):
    """
    Check the SSL expiration date of a given domain.
    """
    try:
        # Create an SSL connection
        cert = ssl.get_server_certificate((domain, 443))
        # Load the certificate
        x509 = ssl.PEM_cert_to_DER_cert(cert)
        # Extract expiration date
        expiration_date = ssl.cert_time_to_seconds(cert['notAfter'])
        return datetime.utcfromtimestamp(expiration_date).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return str(e)


def get_san_domains(domain_or_ip):
    """
    Get all SAN domains from a given domain or IP address.
    """
    try:
        # Send a request to an API to get SAN
        response = requests.get(f"https://api.example.com/san?domain={domain_or_ip}")
        return response.json()  # Assuming the API returns a JSON
    except Exception as e:
        return str(e)


def resolve_domain(domain):
    """
    Resolve a domain to its corresponding IP address.
    """
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return str(e)


def resolve_hostname(ip_address):
    """
    Resolve an IP address to its corresponding hostname.
    """
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror as e:
        return str(e)


def scan_ports(ip_address, port_range=(1, 1024)):
    """
    Scan open ports on a given IP address.
    """
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for connection
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def search_whois(domain_or_ip):
    """
    Search WHOIS information for a given domain or IP address.
    """
    try:
        w = whois.whois(domain_or_ip)
        return {
            "domain": w.domain_name,
            "registrar": w.registrar,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "name_servers": w.name_servers
        }
    except Exception as e:
        return str(e)