# Use the base image for atmoz/sftp
FROM atmoz/sftp

# Install tc (traffic control) for rate limiting
RUN apt-get update && apt-get install -y iproute2

# Set environment variable to configure the SFTP user
ENV SFTP_USERS="<username>:<pwd>:1001:1001"

# Copy custom sshd_config into the container
COPY sshd_config /etc/ssh/sshd_config

# Change the ownership of the upload directory to user 1001 (<username>)
# and give appropriate read/write permissions
RUN mkdir -p /home/<username>/upload && \
    chown -R 1001:1001 /home/<username>/upload && \
    chmod 755 /home/<username>/upload

RUN chown -R 1001:1001 /home/<username> && \
    chmod 755 /home/<username>

# Add a script to set up rate limiting
COPY setup-rate-limit.sh /usr/local/bin/setup-rate-limit.sh
RUN chmod +x /usr/local/bin/setup-rate-limit.sh

# Modify the entrypoint to include rate limiting setup
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D", "-e"]