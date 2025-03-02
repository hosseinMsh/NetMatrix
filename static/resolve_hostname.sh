 # Define colors
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color
resolve_hostname() {
 

    # Check if the required argument is provided
    if [ -z "$1" ]; then
        echo "Usage: resolve_hostname <HOSTNAME_OR_IP>"
        return 1
    fi

    target=$1

    # Check if the target is an IP address
    if [[ $target =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        # Perform a reverse DNS lookup (IP to hostname)
        hostname=$(dig +short -x "$target")
        if [ -z "$hostname" ]; then
            echo -e "${RED}No hostname found for IP address $target.${NC}"
        else
            echo -e "${GREEN}IP address $target resolves to:${NC} $hostname"
        fi
    else
        # Perform a forward DNS lookup (hostname to IP)
        ip_addresses=$(dig +short "$target")
        if [ -z "$ip_addresses" ]; then
            echo -e "${RED}No IP addresses found for hostname $target.${NC}"
        else
            echo -e "${GREEN}Hostname $target resolves to the following IP addresses:${NC}"
            echo "$ip_addresses"
        fi
    fi
}
resolve_hostname "$@"