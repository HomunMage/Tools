# Authentik Installation on Kubernetes

A comprehensive guide to deploying Authentik (open-source identity provider) on Kubernetes with Helm, including SSL certificates and proper secret management.

## Prerequisites

- Kubernetes cluster running
- `kubectl` configured
- `helm` installed
- Domain name (e.g., `authentik.yourdomain.com`)
- SSL certificate and key files

## Step 1: Generate Authentik Secret Key

Authentik requires a secret key for cryptographic operations. Generate a secure random key:

```bash
# Generate a 50-character random secret key
openssl rand -base64 60 | tr -d '\n' && echo
```

**Save this output** - you'll need it in the values.yaml file.

Example output:
```
xK9mP2vL8nQ4rT6wY1zA3bC5dE7fG0hJ2kM4nP6qR8sT0uV2wX4yZ6aB8cD0eF2g
```

## Step 2: Create Namespace

```bash
kubectl create namespace authentik
```

## Step 3: Prepare SSL Certificates

Place your SSL certificate files in your working directory:

```bash
# Your directory structure should look like:
# authentik/
# ├── authentik.yourdomain.com.pem
# ├── authentik.yourdomain.com.key
# ├── values.yaml
# └── authentik-ingress.yaml
```

Create the TLS secret:

```bash
kubectl create secret tls authentik-tls \
  --cert=authentik.yourdomain.com.pem \
  --key=authentik.yourdomain.com.key \
  -n authentik
```

## Step 4: Generate Strong PostgreSQL Password

Generate a secure password for PostgreSQL:

```bash
# Generate a 32-character random password
openssl rand -base64 32 | tr -d '\n' && echo
```

Example output:
```
vR8sT0uV2wX4yZ6aB8cD0eF2gH4jK6mN8pQ
```

## Step 5: Create Helm Values File

Create `values.yaml` with your generated secrets:
<div class="load_as_code_session" data-url="values.yaml">
  Loading content...
</div>

## Step 6: Create Ingress Configuration

Create `authentik-ingress.yaml`:
<div class="load_as_code_session" data-url="authentik-ingress.yaml">
  Loading content...
</div>

## Step 7: Add Authentik Helm Repository

```bash
helm repo add authentik https://charts.goauthentik.io
helm repo update
```

## Step 8: Install Authentik

```bash
helm install authentik authentik/authentik \
  -n authentik \
  -f values.yaml
```

Expected output:
```
NAME: authentik
LAST DEPLOYED: Sun Jan 18 16:36:16 2026
NAMESPACE: authentik
STATUS: deployed
REVISION: 1
```

## Step 9: Monitor Installation Progress

Watch pods starting up:

```bash
kubectl get pods -n authentik -w
```

You should see:
1. `authentik-postgresql-0` - PostgreSQL database
2. `authentik-server-xxxxx` - Authentik web server
3. `authentik-worker-xxxxx` - Authentik background worker

Wait until all pods show `1/1` READY status (this may take 2-3 minutes):

```
NAME                                READY   STATUS    RESTARTS   AGE
authentik-postgresql-0              1/1     Running   0          2m
authentik-server-6b9588c8c4-j6z57   1/1     Running   0          2m
authentik-worker-6d7d749f56-klft2   1/1     Running   0          2m
```

Press `Ctrl+C` to stop watching.

## Step 10: Verify Services

Check that all services are created:

```bash
kubectl get svc -n authentik
```

Expected output:
```
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)
authentik-postgresql   ClusterIP   10.43.xx.xx     <none>        5432/TCP
authentik-redis        ClusterIP   10.43.xx.xx     <none>        6379/TCP
authentik-server       ClusterIP   10.43.xx.xx     <none>        80/TCP,443/TCP
```

## Step 11: Apply Ingress

Once all pods are ready, apply the ingress configuration:

```bash
kubectl apply -f authentik-ingress.yaml
```

Verify ingress:

```bash
kubectl get ingress -n authentik
```

Expected output:
```
NAME        CLASS   HOSTS                       ADDRESS         PORTS     AGE
authentik   nginx   authentik.yourdomain.com   192.168.1.100   80, 443   10s
```

## Step 12: Get Bootstrap Password

Retrieve the initial admin password:

```bash
kubectl get secret -n authentik authentik -o jsonpath='{.data.AUTHENTIK_BOOTSTRAP_PASSWORD}' | base64 -d && echo
```

If that doesn't work, try:

```bash
# List all secrets to find the right one
kubectl get secrets -n authentik

# Try common secret names
kubectl get secret -n authentik authentik-bootstrap-password -o jsonpath='{.data.password}' | base64 -d && echo
```

Save this password - you'll need it for initial login.

## Step 13: Access Authentik

1. Open your browser and navigate to: `https://authentik.yourdomain.com`

2. Log in with:
   - **Username:** `akadmin`
   - **Password:** (from Step 12)

3. You should see the Authentik admin dashboard!

## Step 14: Initial Configuration (Optional but Recommended)

After logging in:

1. **Change the default password:**
   - Click on the user icon (top right)
   - Go to Settings → Password
   - Set a strong new password

2. **Configure email (optional):**
   - Go to System → Settings
   - Configure SMTP settings for password resets and notifications

3. **Create your first application:**
   - Go to Applications → Applications
   - Click "Create" to add your first OAuth2/SAML application

## Troubleshooting

### Pods not starting

Check pod logs:
```bash
kubectl logs -n authentik authentik-server-xxxxx -f
```

### PostgreSQL connection issues

Verify PostgreSQL is running:
```bash
kubectl get pods -n authentik | grep postgresql
kubectl logs -n authentik authentik-postgresql-0
```

### Ingress not working

Check ingress controller:
```bash
kubectl get pods -n ingress-nginx
kubectl logs -n ingress-nginx <ingress-controller-pod>
```

Verify DNS points to your cluster's ingress IP:
```bash
kubectl get ingress -n authentik
nslookup authentik.yourdomain.com
```

### Reset Everything

If you need to start over:
```bash
helm uninstall authentik -n authentik
kubectl delete namespace authentik
# Wait a minute, then start from Step 2
```

## Security Best Practices

1. **Rotate secrets regularly** - Change your secret_key and database passwords periodically
2. **Use Kubernetes secrets** - Consider using sealed-secrets or external-secrets operator for production
3. **Enable 2FA** - Configure multi-factor authentication in Authentik
4. **Regular backups** - Backup your PostgreSQL database regularly
5. **Monitor logs** - Set up log aggregation for security events

## Upgrading Authentik

To upgrade to a newer version:

```bash
helm repo update
helm upgrade authentik authentik/authentik \
  -n authentik \
  -f values.yaml
```

## Conclusion

You now have a fully functional Authentik identity provider running on Kubernetes! You can use it to provide SSO (Single Sign-On) for your applications, manage users, and configure various authentication flows.

Next steps:
- Integrate your first application with Authentik
- Configure user sources (LDAP, OAuth, etc.)
- Set up custom branding
- Configure MFA policies

For more information, visit the [Authentik Documentation](https://docs.goauthentik.io/).



<script src="https://posetmage.com/cdn/js/LoadAsCodeSession.js"></script>
