import socket
import re


def resolve_hostname(target):
    if not target:
        print("Usage: resolve_hostname <HOSTNAME_OR_IP>")
        return

    # بررسی اینکه آیا مقدار ورودی یک IP است یا یک نام دامنه
    ip_pattern = re.compile(r"^\d+\.\d+\.\d+\.\d+$")

    if ip_pattern.match(target):
        # انجام Reverse DNS Lookup (تبدیل IP به نام دامنه)
        try:
            hostname = socket.gethostbyaddr(target)[0]
            print(f"IP address {target} resolves to: {hostname}")
        except socket.herror:
            print(f"No hostname found for IP address {target}.")
    else:
        # انجام Forward DNS Lookup (تبدیل نام دامنه به IP)
        try:
            ip_addresses = socket.gethostbyname_ex(target)[2]
            if ip_addresses:
                print(f"Hostname {target} resolves to the following IP addresses:")
                for ip in ip_addresses:
                    print(ip)
            else:
                print(f"No IP addresses found for hostname {target}.")
        except socket.gaierror:
            print(f"No IP addresses found for hostname {target}.")


# مثال استفاده
resolve_hostname("example.com")
resolve_hostname("8.8.8.8")
