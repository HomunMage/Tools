# Remote Desktop Access to Linux on a Secure SSH Tunnel

In this guide, we'll demonstrate how to securely access a Linux PC from a Windows notebook using Remote Desktop Protocol (RDP) over an SSH tunnel. This approach enhances security by using a non-default SSH port and restricting access to critical services. We’ll handle everything from setting up `xrdp` on the Linux PC to configuring SSH port forwarding via the command line.

---

## XRDP
**Step 1: Install and Configure `xrdp` on the Linux PC**

1. **Install `xrdp`**:
   Open a terminal on your Linux PC and run:
   ```bash
   sudo apt update
   sudo apt install xrdp
   ```

2. **Start and Enable `xrdp`**:
   To ensure `xrdp` starts automatically on boot and is currently running:
   ```bash
   sudo systemctl start xrdp
   sudo systemctl enable xrdp
   ```

---

## SSH
**Step 2: Configure SSH for Key-Based Authentication and Non-Default Port**

1. **Generate SSH Key Pair (on your local machine)**:
   If you don’t already have an SSH key pair, generate one:
   ```bash
   ssh-keygen -t rsa -b 4096
   ```

   Follow the prompts to save the key (default location is `~/.ssh/id_rsa`).

2. **Copy Public Key to the Linux PC**:
   Copy your public key to the Linux PC to enable key-based authentication:
   ```bash
   ssh-copy-id -i ~/.ssh/id_rsa.pub user@linux-pc-ip
   ```

   This command appends your public key to the `~/.ssh/authorized_keys` file on the Linux PC.

3. **Change SSH Port and Configure Authentication**:
   Edit the SSH configuration file on the Linux PC:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```

   Change the port to a non-default value (e.g., 3390):
   ```bash
   Port 3390
   ```

   Ensure only key-based authentication is allowed:
   ```bash
   PasswordAuthentication no
   ChallengeResponseAuthentication no
   UsePAM no
   ```

   Save the changes and restart the SSH service:
   ```bash
   sudo systemctl restart sshd
   ```
---

## firewall
**Step 3: Configure `ufw` for Enhanced Security**

1. **Reset `ufw` Rules**:
   Start fresh by resetting `ufw` rules:
   ```bash
   sudo ufw reset
   ```
2. **Allow SSH on the Non-Default Port**:
   Allow incoming connections on your non-default SSH port (3390):
   ```bash
   sudo ufw allow 3390/tcp
   ```

3. **Allow RDP Only from Localhost**:
   Allow connections to the `xrdp` service only from localhost (127.0.0.1):
   ```bash
   sudo ufw allow from 127.0.0.1 to any port 3389
   ```

4. **Allow SSH Connections for IPv6**:
   If using IPv6, allow SSH connections on the non-default port:
   ```bash
   sudo ufw allow 3390/tcp comment 'Allow SSH on custom port for IPv6'
   ```

6. **Deny Other `xrdp` Connections**:
   Deny all other incoming connections on port 3389:
   ```bash
   sudo ufw deny 3389/tcp
   ```

7. **Enable `ufw`**:
   Enable the firewall with the configured rules:
   ```bash
   sudo ufw enable
   ```

8. **Verify Firewall Rules**:
   Check the status to ensure your rules are applied correctly:
   ```bash
   sudo ufw status verbose
   ```

   **Expected Output**:
   ```plaintext
   To                         Action      From
   --                         ------      ----
   3389                       ALLOW       127.0.0.1
   3390/tcp                   ALLOW       Anywhere
   3390/tcp (v6)              ALLOW       Anywhere (v6)
   ```

---


## Remote Desktop
**Step 4: Create and Use the SSH Tunnel**

1. **Set Up the SSH Tunnel from Windows**:
   Open Command Prompt or PowerShell on your Windows notebook and create the SSH tunnel using the following command:
   ```bash
   ssh -i ~/.ssh/id_rsa -L 3388:127.0.0.1:3389 -p 3390 user@linux-pc-ip
   ```

   - `-i ~/.ssh/id_rsa`: Specifies the private key file for authentication.
   - `-L 3388:127.0.0.1:3389`: Forwards local port 3388 to the remote port 3389 where `xrdp` is listening.
   - `-p 3390`: Uses the non-default SSH port.
   - `user@linux-pc-ip`: Replace with your Linux username and IP address.

   Keep this terminal open to maintain the SSH tunnel.

2. **Connect to Linux Desktop via RDP**:
   Use an RDP client on your Windows notebook (such as Remote Desktop Connection) and connect to:
   ```
   127.0.0.1:3388
   ```

   This will route the RDP connection through the secure SSH tunnel to your Linux desktop.

---

## Conclusion

By following these steps, you have established a secure SSH tunnel from your Windows notebook to your Linux PC for Remote Desktop access. This setup leverages a non-default SSH port, key-based authentication, and local port forwarding to enhance security and ensure that your `xrdp` service is only accessible through a secure connection. This configuration minimizes exposure to potential attacks and provides a safe and efficient way to manage your remote Linux environment.