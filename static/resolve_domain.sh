#!/bin/bash

# Resolve domain to IP
resolve_domain() {
    if [ -z "$1" ]; then
        echo "Usage: resolve_domain <domain>"
        return 1
    fi

    domain=$1

    # Use dig to resolve the domain to IP addresses
    ip_addresses=$(dig +short "$domain")

    if [ -z "$ip_addresses" ]; then
        echo "Could not resolve the domain: $domain"
        return 1
    else
        echo "IP addresses for \"$domain\" is \"$ip_addresses\""
    fi
}

resolve_domain "$@"