import ssl
import socket
from datetime import datetime


def check_ssl_expiration(domain):
    port = 443  # پورت پیش‌فرض SSL

    try:
        # اتصال به سرور و دریافت گواهی SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                cert = ssl_sock.getpeercert()

        # استخراج تاریخ انقضا از گواهی
        expiration_date_str = cert['notAfter']
        expiration_date = datetime.strptime(expiration_date_str, "%b %d %H:%M:%S %Y %Z")
        # محاسبه تعداد روزهای باقی‌مانده تا انقضا
        days_until_expiration = (expiration_date - datetime.now()).days

        if days_until_expiration <= 0:
            print(f"The SSL certificate for {domain} has expired.")
        else:
            print(f"The SSL certificate for {domain} expires in {days_until_expiration} days.")

    except Exception as e:
        print(f"Could not retrieve the SSL certificate for {domain}: {e}")


# مثال استفاده
check_ssl_expiration("sharif.ir")
