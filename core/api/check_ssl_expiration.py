import ssl
import warnings
import socket
from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend

from core.api.get_san_domains import get_san_domains  # Import the function from the first code
from core.api.utilities import DEFAULT_PORTS


def log_warnings(message, category, filename, lineno, file=None, line=None):
    with open("ssl_warnings.log", "a") as log_file:
        log_file.write(f"{category.__name__}: {message} (File: {filename}, Line: {lineno})\n")


warnings.showwarning = log_warnings  # Redirect warnings to the log file


def check_ssl_expiration(domain, port=443):

    if port == "all":
        ports = range(0, 65536)
    elif port == "well known":
        ports = DEFAULT_PORTS
    else:
        ports = [port]

    for p in ports:
        try:
            # Establish connection and retrieve SSL certificate
            context = ssl.create_default_context()
            with socket.create_connection((domain, p), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                    ssl_version = ssl_sock.version()
                    cert_der = ssl_sock.getpeercert(binary_form=True)
                    cert = x509.load_der_x509_certificate(cert_der, default_backend())

            expiration_date = cert.not_valid_after.replace(tzinfo=timezone.utc)
            days_until_expiration = (expiration_date - datetime.now(timezone.utc)).days

            # Replace manual extraction with a call to get_san_domains:
            domains = get_san_domains(domain, p)

            # Check support for lower SSL/TLS versions
            supported_versions = []
            for tls_version, protocol in [
                ("TLSv1", ssl.PROTOCOL_TLSv1),
                ("TLSv1.1", ssl.PROTOCOL_TLSv1_1),
                ("TLSv1.2", ssl.PROTOCOL_TLSv1_2)
            ]:
                try:
                    tls_context = ssl.SSLContext(protocol)
                    with socket.create_connection((domain, p), timeout=5) as sock:
                        with tls_context.wrap_socket(sock, server_hostname=domain) as test_sock:
                            supported_versions.append(tls_version)
                except (ssl.SSLError, socket.timeout):
                    pass
                except AttributeError:
                    continue

            supported_versions_str = ", ".join(supported_versions) if supported_versions else "None"

            print(f"SSL Certificate Details for {domain} on port {p} (using {ssl_version}):")
            for san_domain in domains:
                print(
                    f"  - {san_domain} expires in {days_until_expiration} days ({expiration_date}), supports: {supported_versions_str}")

        except ssl.SSLError:
            print(f"Port {p} on {domain} does not support SSL.")
        except socket.timeout:
            pass
        except Exception as e:
            print(f"Could not retrieve the SSL certificate for {domain} on port {p}: {e}")


# Example usage
check_ssl_expiration("www.lichess.org")
