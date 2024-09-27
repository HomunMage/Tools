#!/bin/bash

# Set up rate limiting
echo "Setting up rate limiting..."
/usr/local/bin/setup-rate-limit.sh
echo "Rate limiting setup complete."

# Print current tc configuration for debugging
echo "Current tc configuration:"
tc qdisc show
tc class show
tc filter show

# Execute the original entrypoint
echo "Executing original entrypoint..."
exec /entrypoint