# SFTP

```
docker run -d \
  --name sftp \
  -p <port>:22 \
  -v "$(pwd)":/home/<username>/upload:ro \
  -e SFTP_USERS=<username>:<pwd> \
  atmoz/sftp
```