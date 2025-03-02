  # Define colors
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color

    # Default important ports
    DEFAULT_PORTS="20,21,22,23,25,53,67,68,80,110,143,161,194,443,465,587,993,995,3306,3389,5432,8000,8080,8443,9000,9200,27017,6379"

scan_ports() {
  

    # Check if the required arguments are provided
    if [ -z "$1" ]; then
        echo "Usage: scan_ports <IP_ADDRESS> [-r <START_PORT> <END_PORT> | -d]"
        return 1
    fi

    ip_address=$1
    shift

    # Check for options
    while [[ $# -gt 0 ]]; do
        case $1 in
            -r) 
                start_port=$2
                end_port=$3
                shift 3
                ;;
            -d) 
                IFS=',' read -r -a ports <<< "$DEFAULT_PORTS"
                shift
                ;;
            *) 
                echo "Invalid option: $2"
                echo "Usage: scan_ports <IP_ADDRESS> [-r <START_PORT> <END_PORT> | -d]"
                return 1
                ;;
        esac
    done

    # If using range, validate ports
    if [[ -n "$start_port" && -n "$end_port" ]]; then
        echo -e "${BLUE}Scanning ports $start_port to $end_port on $ip_address...${NC}"
        for port in $(seq "$start_port" "$end_port"); do
            nc -zv -w 1 "$ip_address" "$port" > /dev/null 2>&1
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}Port $port is open.${NC}"
            else
                echo -e "${RED}Port $port is closed.${NC}"
            fi
        done
    elif [[ -n "${ports[@]}" ]]; then
        echo -e "${BLUE}Scanning important ports on $ip_address...${NC}"
        for port in "${ports[@]}"; do
            nc -zv -w 1 "$ip_address" "$port" > /dev/null 2>&1
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}Port $port is open.${NC}"
            else
                echo -e "${RED}Port $port is closed.${NC}"
            fi
        done
    else
        echo "No valid ports specified for scanning."
        return 1
    fi
}
scan_ports "$@"