FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Install curl so the Docker healthcheck can run
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./


RUN uv pip install -r pyproject.toml --system

COPY . .