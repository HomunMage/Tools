# Simple Authentication for Docker Services

When building services with Docker, securing access to them is often a crucial step. Whether you want to protect an internal API or limit access to a simple web service, you can achieve this with a lightweight authentication layer. In this post, I’ll show you two approaches to add a simple login step to your Docker services.

#### Two Approaches to Authentication:
1. **Nginx Basic Authentication**: Use Nginx as a reverse proxy to protect your services with HTTP basic authentication.
2. **Custom Backend Authentication**: Implement a custom login system in your backend using simple token-based authentication.

By the end, you’ll have a fully functional example where users must log in before accessing your services.

---

## **Approach 1: Nginx Basic Authentication**

This method uses Nginx as a reverse proxy in front of your services, where it asks users for a username and password before allowing access.

#### Step 1: Create the Docker Compose Setup

We will run an Nginx container alongside your other services. Nginx will handle the authentication and forward traffic to your backend or frontend service.

```yaml
version: '3'

services:
  nginx:
    image: nginx:latest
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf   # Custom Nginx configuration
      - ./auth:/etc/nginx/.htpasswd          # .htpasswd file for authentication
    ports:
      - "80:80"                              # Expose Nginx on port 80
    restart: always                          # Restart the service if it fails

  backend:
    image: node:14                           # Example backend using Node.js
    volumes:
      - ./backend:/usr/src/app               # Mount the backend directory
    ports:
      - "8080:8080"                          # Expose the backend on port 8080
    command: "node server.js"                # Command to start the backend
    restart: always
```

This setup assumes you have a `backend` service that you want to protect. The Nginx container will handle authentication before proxying requests to it.

#### Step 2: Configure Nginx for Basic Authentication

In your `nginx.conf`, you’ll need to enable basic authentication and set up Nginx to forward requests to your backend.

```nginx
server {
    listen 80;

    location / {
        # Enable basic authentication
        auth_basic "Protected Area";
        auth_basic_user_file /etc/nginx/.htpasswd;

        # Proxy requests to the backend service
        proxy_pass http://backend:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### Step 3: Create the `.htpasswd` File

Solution1:

To create a username and password for basic authentication, you’ll use the `htpasswd` tool. This file will store the credentials in an encrypted format.

```bash
docker run --rm --entrypoint htpasswd httpd:2 -c ./auth/.htpasswd user1
```

This command will prompt you for a password for `user1` and create the `.htpasswd` file in the `./auth/` directory.

Solution2:
```bash
docker run --rm httpd:alpine htpasswd -nbB username password

```

#### Step 4: Start the Services

Now, you can start your services using Docker Compose:

```bash
docker-compose up -d
```

When users visit `http://localhost`, they’ll be prompted for a username and password. Only after successful authentication will they be forwarded to the backend.

---

## **Approach 2: Custom Backend Authentication**

In some cases, you may want more control over the authentication flow. Instead of relying on Nginx, you can implement a simple token-based login system in your backend.

#### Step 1: Docker Compose Setup

We’ll use a backend service written in Node.js to handle the login process and return a token upon successful authentication.

```yaml
version: '3'

services:
  backend:
    image: node:14
    volumes:
      - ./backend:/usr/src/app
    ports:
      - "8080:8080"
    command: "node server.js"
    restart: always
```

This setup only includes the backend, but you can add other services (such as a frontend) and secure them in a similar way.

#### Step 2: Backend Code with Token Authentication

Here’s a simple example of a Node.js server (`server.js`) that implements token-based authentication. When the user logs in, a token is generated and sent back to the client. This token must be included in subsequent requests to access protected routes.

##### `server.js` (Node.js Backend):
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const jwt = require('jsonwebtoken');

const SECRET_KEY = 'your-secret-key';

app.use(bodyParser.json());

let users = [
  { username: 'user1', password: 'password123' }
];

// Login route
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  const user = users.find(u => u.username === username && u.password === password);
  if (!user) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }

  const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
  return res.json({ token });
});

// Protected route
app.get('/protected', (req, res) => {
  const authHeader = req.headers.authorization;
  
  if (!authHeader) {
    return res.status(401).json({ message: 'No token provided' });
  }

  const token = authHeader.split(' ')[1];
  jwt.verify(token, SECRET_KEY, (err, user) => {
    if (err) {
      return res.status(403).json({ message: 'Invalid token' });
    }
    return res.json({ message: 'Welcome to the protected route!', user });
  });
});

app.listen(8080, () => {
  console.log('Backend running on port 8080');
});
```

#### Step 3: Interacting with the Backend

To interact with this backend:
1. First, the client sends a POST request to `/login` with the username and password.
2. If the login is successful, the server returns a token.
3. The client must include this token in the `Authorization` header (as `Bearer <token>`) for subsequent requests to access protected routes.

##### Example Login Request:
```bash
curl -X POST http://localhost:8080/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "password123"}'
```

This returns a JSON response with the token:
```json
{
  "token": "your.jwt.token"
}
```

##### Accessing a Protected Route:
Once logged in, you can access protected routes by passing the token in the `Authorization` header:
```bash
curl -X GET http://localhost:8080/protected \
  -H "Authorization: Bearer your.jwt.token"
```

If the token is valid, you will receive access to the route.

---

### Conclusion

Both approaches offer simple ways to add authentication to your Docker services.

1. **Nginx Basic Authentication** is a fast and easy solution that doesn’t require changes to your backend but has limited flexibility.
2. **Custom Backend Authentication** provides more control and can be extended with additional security features, such as session management or role-based access control.

You can choose the solution that best fits your project’s needs. For quick protection of internal services, Nginx basic authentication works well. For more complex applications, a custom backend authentication system is often a better choice.

Feel free to try both approaches and let me know how it works for your project!
