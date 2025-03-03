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

