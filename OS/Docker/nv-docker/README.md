# NVIDIA Docker 

Use ollama as example:

## Dockerfile
you need nvidia/cuda:12.2.0-base-ubuntu22.04

<div class="load_as_code_session" data-url="Dockerfile">
  Loading content...
</div>

use this Dockerfile:  
```
docker build -t ollama .
docker create --gpus all -it --name ollama ollama /bin/bash

```
the file init_ollama.sh
<div class="load_as_code_session" data-url="init_ollama.sh">
  Loading content...
</div>


## Docker Compose
docker-compose.yml

<div class="load_as_code_session" data-url="docker-compose.yml">
  Loading content...
</div>


<script src="{{ '/assets/js/LoadAsCodeSession.js' | relative_url }}"></script>
