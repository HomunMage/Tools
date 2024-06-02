# Use the official Ubuntu image as the base
FROM ubuntu:latest

# Install SSH server
RUN apt-get update && apt-get install -y openssh-server sudo

# Set up the user and add to sudo group
ARG SSH_USERNAME
ARG SSH_PASSWORD
RUN useradd -m -s /bin/bash ${SSH_USERNAME} && \
    echo "${SSH_USERNAME}:${SSH_PASSWORD}" | chpasswd && \
    adduser ${SSH_USERNAME} sudo

# Set up SSH to accept connections
RUN mkdir /var/run/sshd
RUN echo 'PermitRootLogin no' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config
RUN echo "AllowUsers ${SSH_USERNAME}" >> /etc/ssh/sshd_config
RUN mkdir -p /home/${SSH_USERNAME}/.ssh
RUN chown ${SSH_USERNAME}:${SSH_USERNAME} /home/${SSH_USERNAME}/.ssh
RUN chmod 700 /home/${SSH_USERNAME}/.ssh

# Expose the SSH port
EXPOSE 22

# Run the SSH server
CMD ["/usr/sbin/sshd", "-D"]
