import subprocess
import re


def ping_ip(ip_address, packet_count=4):
    try:
        result = subprocess.run([
            "ping", "-c", str(packet_count), ip_address
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output = result.stdout

        if "100% packet loss" in output:
            print(f"\033[91mIP address {ip_address} is not reachable.\033[0m")
            return False

        match = re.search(r'min/avg/max/mdev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+)', output)
        if match:
            avg_ping = match.group(2)
            print(f"\033[92mIP address {ip_address} is reachable.\033[0m "
                  f"\033[94mAverage ping over {packet_count} packets: \033[93m{avg_ping} ms\033[0m")
            return True
        else:
            print(f"\033[91mCould not extract ping statistics for {ip_address}.\033[0m")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    ip = "8.8.8.8"  # آدرس IP برای تست
    ping_ip(ip)
