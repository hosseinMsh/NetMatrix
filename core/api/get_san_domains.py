import ssl
import socket
from cryptography import x509
from cryptography.hazmat.backends import default_backend


def get_san_domains(domain, port=443, print_domains=False):
    """
    Retrieves the Subject Alternative Names (SAN) from the SSL certificate
    of the given domain. If retrieval fails, returns a list containing the original domain.

    Parameters:
        domain (str): The target domain to retrieve SAN from.
        port (int): The port to use for the SSL connection (default: 443).
        print_domains (bool): If True, prints the retrieved domains (default: False).

    Returns:
        list: A list of SAN domains.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert_der = ssock.getpeercert(binary_form=True)
        cert = x509.load_der_x509_certificate(cert_der, default_backend())
        san_extension = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        domains = san_extension.value.get_values_for_type(x509.DNSName)

        if print_domains:
            print(f"Subject Alternative Names for {domain}:")
            for d in domains:
                print(f"  - {d}")

        return domains
    except Exception as e:
        print(f"Error retrieving SAN domains from {domain}: {e}")
        return [domain]


if __name__ == "__main__":
    target_domain = "www.lichess.org"  # Change to your target domain
    # Call the function with print_domains=True to print the retrieved domains.
    san_domains = get_san_domains(target_domain, print_domains=True)
