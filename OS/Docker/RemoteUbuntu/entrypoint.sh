#!/bin/bash

# Start SSH service
service ssh start

# Execute any additional commands or services
# e.g., start other services or run applications

# Keep the container running
exec "$@"
