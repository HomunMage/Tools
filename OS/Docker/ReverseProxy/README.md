# Nginx Reverse Proxy with Multiple Docker Compose Services

---

**Introduction:**

When using services like Cloudflare, which only accepts traffic over port 443 (HTTPS), handling multiple URLs on the same IP can become challenging. In such cases, you need a reverse proxy to route incoming requests to the appropriate service based on the domain name or URL. This is where **Nginx reverse proxy** comes in handy, enabling you to direct traffic to different Docker services running on the same machine. In this guide, we'll walk through setting up Nginx as a reverse proxy for multiple Docker Compose stacks, all using external Docker networks to allow the containers to communicate.

---

### Why Use an Nginx Reverse Proxy?

A reverse proxy like Nginx acts as a gatekeeper for incoming traffic, directing it to the right backend service. The key advantages of this setup include:

1. **Single Entry Point**: All incoming traffic goes through Nginx, which can forward requests to the correct service based on the domain.
2. **Multiple Services on One IP**: You can run multiple services on the same machine and IP address, even if Cloudflare (or any external service) only allows port 443.
3. **Simplified SSL Management**: You only need to manage SSL certificates in one place (Nginx), even though multiple services are running.

---

### Step 1: Setting Up an External Network for Communication

To allow multiple Docker Compose stacks to communicate, you need to create an external Docker network. This allows the services in different `docker-compose.yml` files to see and connect to each other.

Run the following command to create the external network:

```bash
docker network create shared-network
```

This network will be referenced in all Docker Compose files.

---

### Step 2: Nginx Reverse Proxy Docker Compose

First, let’s create a `docker-compose.yml` for Nginx that will act as a reverse proxy. This file will listen on port 443 and forward requests to the correct backend services based on the domain.

Here’s an example of a basic Nginx reverse proxy setup:

```yaml
version: '3'
services:
  nginx-proxy:
    image: nginx:latest
    container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    networks:
      - shared-network

networks:
  shared-network:
    external: true
```

In this setup:

- We expose ports 80 (HTTP) and 443 (HTTPS).
- We mount the Nginx configuration file (`nginx.conf`) and SSL certificates directory (`certs`).
- The service is attached to the `shared-network`, which is external and will be shared across different stacks.

#### Nginx Configuration (`nginx.conf`):

You need to configure Nginx to route traffic based on the domain name. Here’s an example `nginx.conf`:

```nginx
events {}

http {
    server {
        listen 443 ssl;
        server_name example.com;

        ssl_certificate /etc/nginx/ssl/example.crt;
        ssl_certificate_key /etc/nginx/ssl/example.key;

        location / {
            proxy_pass http://service1:8081;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

    server {
        listen 443 ssl;
        server_name another-example.com;

        ssl_certificate /etc/nginx/ssl/another-example.crt;
        ssl_certificate_key /etc/nginx/ssl/another-example.key;

        location / {
            proxy_pass http://service2:8082;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

---

### Step 3: Configuring the Docker Compose Stacks for Services

Now that the reverse proxy is set up, let’s configure two services that Nginx will route traffic to. Each service will have its own `docker-compose.yml` file.

#### Docker Compose for Service 1:

```yaml
version: '3'
services:
  service1:
    image: myapp1:latest
    container_name: service1
    ports:
      - "127.0.0.1:8081:8080"
    networks:
      - shared-network

networks:
  shared-network:
    external: true
```

#### Docker Compose for Service 2:

```yaml
version: '3'
services:
  service2:
    image: myapp2:latest
    container_name: service2
    ports:
      - "127.0.0.1:8082:8080"
    networks:
      - shared-network

networks:
  shared-network:
    external: true
```

---

### Step 4: Running the Setup

To bring up the Nginx reverse proxy and the services, follow these steps:

1. **Start Nginx Reverse Proxy**:
   Navigate to the directory where the Nginx `docker-compose.yml` file is located and run:

   ```bash
   docker-compose up -d
   ```

2. **Start Each Service**:
   For each service, navigate to its respective directory and run:

   ```bash
   docker-compose up -d
   ```

---

### Step 5: Testing the Setup

Now, when you access `https://example.com`, the request should be routed to Service 1. Similarly, accessing `https://another-example.com` should route traffic to Service 2. Nginx is acting as the reverse proxy, forwarding requests to the appropriate services based on the domain.

---

### Conclusion

Setting up an Nginx reverse proxy with Docker Compose allows you to host multiple services on the same server behind a single IP address. By leveraging external Docker networks, you can easily manage communication between different services across different `docker-compose` stacks. This setup is perfect for cases like Cloudflare, where only port 443 is allowed, and multiple domains need to be served from the same IP.
