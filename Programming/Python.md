# Useful python tools

```Dockerfile
# Build stage: install deps in uv image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Runtime stage: minimal image
FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends cron supervisor && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy Python + venv from builder
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy source
COPY ./src/ ./src/
RUN mkdir -p /app/src/workspace /app/src/log

# Cron
COPY daily.sh daily.sh
RUN chmod +x /app/daily.sh
COPY crontab /mycron
RUN chmod 644 /mycron && crontab /mycron

# Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
```

```python
# flatten list of list
list(itertools.chain.from_iterable(list_of_lists))
# Cartesian product
itertools.product()
# char to number, number to char
ord(c)
chr(number)
# is number
isnumeric()
```

```python
from collections import defaultdict, Counter

input_string = "hello world"

# 3. Using collections.Counter
dict_cnt = Counter(input_string)

# 2. Using defaultdict(int)
dict_cnt = defaultdict(int)
for char in input_string:
    dict_cnt[char] += 1

# 1. Using for...in (with a regular dictionary)
dict_cnt = {}
for char in input_string:
    dict_cnt:
        dict_cnt[char] += 1
    else:
        dict_cnt[char] = 1
```
