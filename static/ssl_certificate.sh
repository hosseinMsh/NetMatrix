#!/bin/bash

# Function to check SSL certificate expiration
check_ssl_expiration() {
    if [ -z "$1" ]; then
        echo "Usage: check_ssl_expiration <domain>"
        return 1
    fi

    domain=$1
    port=443

    # Get the SSL certificate expiration date
    expiration_date=$(echo | openssl s_client -servername $domain -connect $domain:$port 2>/dev/null | openssl x509 -noout -enddate | cut -d= -f2)

    if [ -z "$expiration_date" ]; then
        echo "Could not retrieve the SSL certificate for $domain"
        return 1
    fi

    # Convert the expiration date to a timestamp
    expiration_timestamp=$(date -d "$expiration_date" +%s)
    current_timestamp=$(date +%s)

    # Calculate the number of days until expiration
    days_until_expiration=$(( (expiration_timestamp - current_timestamp) / 86400 ))

    if [ $days_until_expiration -le 0 ]; then
        echo "The SSL certificate for $domain has expired."
    else
        echo "The SSL certificate for $domain expires in $days_until_expiration days."
    fi
}

# Call the function with the domain passed as a script argument
if [ -z "$1" ]; then
    echo "Error: No domain provided."
    echo "Usage: ./ssl_checker.sh <domain>"
    exit 1
fi

check_ssl_expiration "$@"

