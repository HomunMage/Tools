# Setup HTTPS server

Need auto pem, key

## Cloudflare

To ensure your website's security by encrypting traffic between your visitors, Cloudflare, and your origin server, you can set Cloudflare to use Full (Strict) SSL/TLS mode. Here's a step-by-step guide to help you configure it:

### Steps to Configure Full (Strict) SSL/TLS on Cloudflare

set to Full(Strict)

1. **Log In to Cloudflare:**
   - Access your [Cloudflare account](https://dash.cloudflare.com).

2. **Select Your Domain:**
   - Choose the domain you want to configure from your Cloudflare dashboard.

3. **Navigate to SSL/TLS Settings:**
   - Go to the **SSL/TLS** section from the left-hand menu.

4. **Set SSL/TLS Encryption Mode:**
   - In the SSL/TLS settings, find the **"SSL/TLS encryption mode"** section.
   - Select **"Full (Strict)"** to ensure that both Cloudflare and your origin server use valid SSL certificates.


### Using a Certificate Authority

- **Purchase a certificate** from a CA and download the `.pem` (certificate) and `.key` (private key) files.

Using Cloudflare Origin Certificate:

- **Generate an Origin Certificate** from Cloudflare:
  - Log in to Cloudflare.
  - Navigate to the **SSL/TLS** tab.
  - Go to the **"Origin Server"** section.
  - Click **"Create Certificate"**.
  - Follow the instructions to generate a certificate and download the `.pem` and `.key` files.


### Files
put `mydomain.com.key` and `mydomain.com.pem` at `nginx/ssl`


## Nginx

### login password

```
docker run --rm httpd:alpine htpasswd -nb <username> <password>
```
store the content at `nginx/htpasswd/.htpasswd`

one account one line


### Dockerfile
<div class="load_as_code_session" data-url="Dockerfile">
  Loading content...
</div>

### Doker Compose
<div class="load_as_code_session" data-url="docker-compose.yml">
  Loading content...
</div>

### nginx/nginx.conf
<div class="load_as_code_session" data-url="nginx/nginx.conf">
  Loading content...
</div>

<script src="{{ '/assets/js/LoadAsCodeSession.js' | relative_url }}"></script>
