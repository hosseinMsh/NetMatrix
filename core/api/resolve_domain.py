import socket


def resolve_domain(domain):
    if not domain:
        print("Usage: resolve_domain <domain>")
        return

    try:
        # دریافت اطلاعات مربوط به دامنه
        addresses = socket.getaddrinfo(domain, None)

        # استخراج و نمایش آدرس‌های IP
        ip_addresses = set(info[4][0] for info in addresses)

        if ip_addresses:
            print(f'IP addresses for "{domain}": {", ".join(ip_addresses)}')
        else:
            print(f"Could not resolve the domain: {domain}")

    except socket.gaierror:
        print(f"Could not resolve the domain: {domain}")


# مثال استفاده
resolve_domain("example.com")
