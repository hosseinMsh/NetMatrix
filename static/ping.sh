#!/bin/bash

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default packet count
    packet_count=2

# Function to ping an IP address
ping_ip() {
    

    # Parse arguments
    while getopts ":c:" opt; do
        case $opt in
            c) packet_count="$OPTARG" ;;
            *) echo "Usage: ping_ip [-c <packet_count>] <IP_ADDRESS>"; return 1 ;;
        esac
    done
    shift $((OPTIND - 1))

    if [ -z "$1" ]; then
        echo "Usage: ping_ip [-c <packet_count>] <IP_ADDRESS>"
        return 1
    fi

    ip_address=$1

    # Ping the IP address with the specified packet count
    ping_output=$(ping -c "$packet_count" "$ip_address" 2>&1)

    # Check if the ping was successful
    if echo "$ping_output" | grep -q "100% packet loss"; then
        echo -e "${RED}IP address $ip_address is not reachable.${NC}"
        return 1
    else
        # Extract the average ping time from the output
        avg_ping=$(echo "$ping_output" | grep -oP 'min/avg/max/mdev = \K[\d.]+/[0-9.]+/[0-9.]+/[0-9.]+' | cut -d '/' -f 2)
        echo -e "${GREEN}IP address $ip_address is reachable.${NC} ${BLUE}Average ping over ${packet_count} packets: ${YELLOW}${avg_ping} ms${NC}"
    fi
}

# Main script logic
while [[ $# -gt 0 ]]; do
    case $1 in
        -c) packet_count="$2"; shift 2 ;;
        *) ip_address="$1"; shift ;;
    esac
done

# Call the ping_ip function with the parsed arguments
if [ -n "$ip_address" ]; then
    ping_ip -c "$packet_count" "$ip_address"
else
    echo "Error: No IP address provided."
    echo "Usage: $0 [-c <packet_count>] <IP_ADDRESS>"
    exit 1
fi