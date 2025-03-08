import re
import logging

logger = logging.getLogger(__name__)


def is_valid_ip(ip):
    # Regular expression pattern for a valid IP address
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if ip_pattern.match(ip):
        # Check if each octet is between 0 and 255
        octets = ip.split('.')
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                logger.warning(f"Invalid octet in IP address: {ip}")
                return False
        logger.info(f"Valid IP address: {ip}")
        return True
    logger.warning(f"Invalid IP address format: {ip}")
    return False


def check_ip(ip):
    if ip:
        if is_valid_ip(ip):
            logger.info(f"Valid IP address: {ip}")
        else:
            logger.error(f"Invalid IP address: {ip}")
    else:
        logger.error("Could not retrieve IP address.")


DEFAULT_PORTS = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 135, 137, 138, 139, 143, 161, 162, 179, 194,
                 389, 443,
                 465, 512, 513, 514, 515, 526, 530, 531, 532, 540, 543, 544, 548, 554, 556, 563, 587, 591, 593, 636,
                 993, 995,
                 1080, 1194, 1433, 1434, 1521, 1701, 1723, 2049, 2082, 2083, 2086, 2087, 2095, 2096, 2181, 3306, 3389,
                 3690,
                 4000, 4045, 4444, 4658, 5000, 5432, 5900, 5985, 5986, 6379, 6665, 6666, 6667, 6668, 6669, 8000, 8080,
                 8443,
                 8888, 9000, 9090, 9200, 9300, 10000, 11211, 27017, 27018, 27019, 50000, 50070]
