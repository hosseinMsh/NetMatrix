import ssl
import warnings
import socket
from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend


# SSL Expiry,version and ports function
# Finds All other domains in the same IP Address from the given domain and returns the properties above
def log_warnings(message, category, filename, lineno, file=None, line=None):
    with open("ssl_warnings.log", "a") as log_file:
        log_file.write(f"{category.__name__}: {message} (File: {filename}, Line: {lineno})\n")


warnings.showwarning = log_warnings  # Redirect warnings to the log file


def check_ssl_expiration(domain, port=443):
    well_known_ports = [
        20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 135, 137, 138, 139, 143, 161, 162, 179, 194, 389, 443,
        465, 512, 513, 514, 515, 526, 530, 531, 532, 540, 543, 544, 548, 554, 556, 563, 587, 591, 593, 636, 993, 995,
        1080, 1194, 1433, 1434, 1521, 1701, 1723, 2049, 2082, 2083, 2086, 2087, 2095, 2096, 2181, 3306, 3389, 3690,
        4000, 4045, 4444, 4658, 5000, 5432, 5900, 5985, 5986, 6379, 6665, 6666, 6667, 6668, 6669, 8000, 8080, 8443,
        8888, 9000, 9090, 9200, 9300, 10000, 11211, 27017, 27018, 27019, 50000, 50070
    ]

    if port == "all":
        ports = range(0, 65536)
    elif port == "well known":
        ports = well_known_ports
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

            san_extension = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
            domains = san_extension.value.get_values_for_type(x509.DNSName)

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
#check_ssl_expiration("172.26.137.192")

