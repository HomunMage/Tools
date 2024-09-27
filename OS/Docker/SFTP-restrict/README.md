# SFTP with restricted speed

the key is let nc work in container
```
    cap_add:
      - NET_ADMIN  # Add NET_ADMIN capability
```
### Docker Compose

<div class="load_as_code_session" data-url="docker-compose.yml">
  Loading content...
</div>

## rate limited

modify ```64mbit``` to what you want to limited speed

### setup-rate-limit.sh

<div class="load_as_code_session" data-url="setup-rate-limit.sh">
  Loading content...
</div>



### Dockerfile

<div class="load_as_code_session" data-url="Dockerfile">
  Loading content...
</div>

### entrypoint.sh

<div class="load_as_code_session" data-url="entrypoint.sh">
  Loading content...
</div>



### sshd_config

<div class="load_as_code_session" data-url="sshd_config">
  Loading content...
</div>


<script src="{{ '/assets/js/LoadAsCodeSession.js' | relative_url }}"></script>
