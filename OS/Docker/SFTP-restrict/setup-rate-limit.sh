#!/bin/bash

# Enable error reporting
set -e

# Find the correct network interface
INTERFACE=$(ip -o -4 route show to default | awk '{print $5}')
echo "Using interface: $INTERFACE"

# Set up rate limiting for the SFTP user
echo "Setting up rate limiting..."

# Clear existing qdiscs
tc qdisc del dev $INTERFACE root >/dev/null 2>&1 || true
tc qdisc del dev $INTERFACE ingress >/dev/null 2>&1 || true

# Set up ingress qdisc
tc qdisc add dev $INTERFACE handle ffff: ingress

# Set up egress qdisc
tc qdisc add dev $INTERFACE root handle 1: htb default 10

# Set up classes
tc class add dev $INTERFACE parent 1: classid 1:1 htb rate 64mbit ceil 64mbit burst 15k
tc class add dev $INTERFACE parent 1:1 classid 1:10 htb rate 64mbit ceil 64mbit burst 15k

# Set up filter for egress
tc filter add dev $INTERFACE protocol ip parent 1:0 prio 1 u32 match ip dst 0.0.0.0/0 flowid 1:10

# Set up filter for ingress
tc filter add dev $INTERFACE parent ffff: protocol ip u32 match u32 0 0 police rate 64mbit burst 15k drop flowid :1

echo "Rate limiting setup complete."

# Print current tc configuration
echo "Current tc configuration:"
tc qdisc show dev $INTERFACE
tc class show dev $INTERFACE
tc filter show dev $INTERFACE