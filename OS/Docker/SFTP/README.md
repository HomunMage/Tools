# SFTP

https://github.com/atmoz/sftp

## Simple start
```
docker run -d \
  --name sftp \
  -p <port>:22 \
  -v "$(pwd)":/home/<username>/share:ro \
  -e SFTP_USERS=<username>:<pwd> \
  atmoz/sftp
```

### DNS
Step-by-Step DNS Setup in Cloudflare

1. **Log in to Cloudflare**
   - Go to Cloudflare (https://www.cloudflare.com) and log into your account.

2. **Navigate to DNS Settings**
   - Select your domain.
   - In the left-hand menu, click on the "DNS" tab to open the DNS settings.

3. **Add an A Record**
   - **Type**: Select **A** from the dropdown.
   - **Name**: Enter the subdomain (e.g., `server` for `server.mydomain.com`).
   - **IPv4 Address**: Enter your server's public IP address.
   - **TTL**: Set to **Auto**.
   - **Proxy Status**: Set to **DNS only** (gray cloud).

4. **Save Your Settings**
   - Click **Save** to apply your DNS record.

5. **Test DNS Setup**
   - After a few minutes, use tools like WhatsMyDNS to verify that your subdomain resolves to the correct IP.



## SFTP Server Using Docker with `.ppk` Key Authentication

In this guide, we’ll set up a simple and secure SFTP (Secure File Transfer Protocol) server using Docker. We will configure it to authenticate users via `.ppk` keys, which are often used with Windows-based SFTP clients like FileZilla.

#### Why Use Docker for SFTP?

Docker makes it easy to set up and run isolated services like an SFTP server without directly installing software on your system. Using Docker simplifies the process of managing and maintaining the SFTP server, ensuring it runs in a contained environment.

---

#### Step 1: Generate SSH Keys

Before starting, you'll need an SSH key pair for secure access to the server.

1. **Generate an RSA key pair** on your Linux machine using the command below:
   ```bash
   ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
   ```
   This generates two files:
   - `~/.ssh/id_rsa`: Your private key (keep this secure).
   - `~/.ssh/id_rsa.pub`: Your public key (used for authentication).

2. **Convert the private key to `.ppk` format** (required for Windows):
   - Install **PuTTYgen** (if you don't have it installed).
   - Open PuTTYgen, load the `id_rsa` private key.
   - Save it as a `.ppk` file by clicking "Save private key."

Now, you have a `.ppk` file that will be used for authentication in Windows clients like FileZilla.

---

#### Step 2: Set Up the Docker SFTP Container

Next, we’ll set up the Docker container for the SFTP server and configure it to use the SSH public key for authentication.

1. **Run the SFTP Docker container**:

   ```bash
   docker run -d \
     --name sftp-server \
     -v "$(pwd)/id_rsa.pub":/home/<username>/.ssh/keys/id_rsa.pub:ro \
     -v "$(pwd)":/home/<username>/upload \
     -p <port>:22 \
     atmoz/sftp \
     <username>::1001
   ```

   Replace:
   - `<port>` with the port you want to expose for SFTP (e.g., 2022).
   - `<username>` with the desired username for the SFTP user.

   This command will:
   - Mount your `id_rsa.pub` file into the container for key-based authentication.
   - Mount the current directory to the SFTP user’s upload folder.
   - Expose the specified port to allow SFTP connections.

---

#### Step 3: Configure FileZilla to Use the `.ppk` Key

Now that your Docker container is running, you can connect to the SFTP server using an SFTP client like FileZilla.

1. **Open FileZilla** and go to **Edit > Settings > SFTP**.
2. Click **Add key file**, select your `.ppk` file, and add it to FileZilla.
3. In **File > Site Manager**, create a new site with the following settings:
   - **Host**: Your server’s IP address.
   - **Port**: The port you set in the Docker run command.
   - **Protocol**: SFTP.
   - **Logon Type**: Interactive.
   - **User**: The username you set in the Docker command.

Now, connect and start transferring files securely!

---

#### Troubleshooting Permissions

If you encounter any file permission issues, ensure the folder on your host system has the correct ownership:

```bash
sudo chown 1001:1001 /path/to/upload
sudo chmod 755 /path/to/upload
```

This ensures the SFTP user inside the container has the correct access rights.

---

#### Conclusion

You’ve now set up a secure SFTP server using Docker and `.ppk` key-based authentication. This setup allows for encrypted file transfers while keeping things simple and manageable. By using Docker, you isolate the SFTP service from your host system, making it easier to control and maintain.
