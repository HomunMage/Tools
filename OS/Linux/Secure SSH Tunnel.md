# Secure SSH Tunnel

In today’s digital landscape, securing your remote connections is paramount. One effective way to achieve this is by using SSH tunnels. This guide will walk you through setting up a secure SSH tunnel by changing the default SSH port, configuring UFW (Uncomplicated Firewall) to restrict access, enforcing key-based authentication, and using port forwarding to connect securely.

## Change the SSH Port

By default, SSH operates on port 22, making it a common target for automated attacks. Changing the SSH port to a non-default value can significantly reduce the likelihood of unauthorized access attempts.

### How to Change the SSH Port

1. **Edit the SSH Configuration**:
   Open your SSH configuration file with a text editor. For example:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```

2. **Set a New Port**:
   Find the line that specifies the port (usually `Port 22`) and change it to a new, non-standard port, such as 4444:
   ```bash
   Port 4444
   ```

3. **Restart the SSH Service**:
   After saving the changes, restart the SSH service to apply the new port setting:
   ```bash
   sudo systemctl restart sshd
   ```

## Allowing SSH Key-Only Authentication

Using SSH key-based authentication is a more secure method than traditional password logins. By disabling password authentication, you can further enhance your server’s security.

### Steps to Enable Key-Only Authentication

1. **Generate an SSH Key Pair** (if you haven't already):
   On your local machine, run:
   ```bash
   ssh-keygen -t rsa -b 4096
   ```
   Follow the prompts to save the key (the default location is usually `~/.ssh/id_rsa`).

2. **Copy Your Public Key to the Linux PC**:
   Use the following command to copy your public key to the Linux PC:
   ```bash
   ssh-copy-id -i ~/.ssh/id_rsa.pub user@your-linux-ip -p 4444
   ```

3. **Edit the SSH Configuration**:
   Open the SSH configuration file again:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```

4. **Disable Password Authentication**:
   Find the following lines and modify them as shown:
   ```bash
   PasswordAuthentication no
   ChallengeResponseAuthentication no
   UsePAM no
   ```

5. **Restart the SSH Service**:
   Save the changes and restart the SSH service:
   ```bash
   sudo systemctl restart sshd
   ```

## Configuring UFW for Enhanced Security

Using UFW is a great way to manage your firewall settings easily. We’ll set it up to allow connections only from localhost for specific services, further securing your server.

### Steps to Configure UFW

1. **Reset UFW Rules**:
   Start with a clean slate by resetting the UFW rules:
   ```bash
   sudo ufw reset
   ```

2. **Allow the New SSH Port**:
   Permit incoming connections on your new SSH port:
   ```bash
   sudo ufw allow 4444/tcp
   ```

3. **Restrict RDP Access**:
   If you’re using RDP (Remote Desktop Protocol) or similar services, restrict access to localhost only. For example, if you choose port 5599 for RDP:
   ```bash
   sudo ufw allow from 127.0.0.1 to any port 5599
   ```

4. **Deny Other Incoming Connections**:
   Deny connections to the default RDP port from all other IP addresses:
   ```bash
   sudo ufw deny 3389/tcp
   ```

5. **Enable UFW**:
   Enable UFW with the new rules:
   ```bash
   sudo ufw enable
   ```

6. **Verify the Configuration**:
   Check your firewall status to ensure that the rules are applied correctly:
   ```bash
   sudo ufw status verbose
   ```

   **Expected Output**:
   ```plaintext
   To                         Action      From
   --                         ------      ----
   5599                       ALLOW       127.0.0.1
   4444/tcp                   ALLOW       Anywhere
   ```

## Connecting Through Port Forwarding

Once your SSH port is changed and your firewall is configured, you can connect to your services securely via port forwarding. This technique allows you to tunnel traffic through your secure SSH connection.

### Steps for Port Forwarding

1. **Establish the SSH Tunnel**:
   From your local machine (Windows, for instance), open your command line interface and create an SSH tunnel. Use the following command:
   ```bash
   ssh -L 6000:127.0.0.1:5599 -p 4444 user@your-linux-ip
   ```
   - `-L 6000:127.0.0.1:5599`: This forwards local port 6000 to the remote port 5599 (where your service is running).
   - `-p 4444`: Connects using the non-default SSH port.
   - Replace `user` and `your-linux-ip` with your actual username and Linux machine's IP address.

2. **Access Your Service**:
   After establishing the tunnel, you can access the service (e.g., RDP) by connecting to:
   ```plaintext
   127.0.0.1:6000
   ```
   This directs your connection through the secure SSH tunnel to the Linux PC.

## Conclusion

By following these steps, you can enhance your remote connection security using SSH tunnels. Changing the SSH port, enforcing key-based authentication, configuring UFW to limit access, and utilizing port forwarding are essential practices for anyone looking to safeguard their remote interactions. This approach not only minimizes exposure to potential attacks but also creates a robust framework for managing remote services securely.

Feel free to share your experiences or any additional tips in the comments below!