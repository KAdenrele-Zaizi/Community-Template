# Dev Container setup

This repository includes a Compose-based VS Code devcontainer for full-stack development.

## What it starts

When you open in container, VS Code starts:

- `devcontainer` (your interactive workspace container)
- `postgres`
- `seaweed`

The `devcontainer` service is built from `backend/Dockerfile` and mounts the full repository at `/workspaces/Community-Template`.

## First run behavior

- If `.env` is missing and `dummy_env` exists, the setup copies `dummy_env` to `.env`.
- Dependencies are installed automatically:
  - Backend: `uv pip install -r pyproject.toml --system`
  - Frontend: `npm install`

## Typical workflow inside the container

Run backend:

- `cd backend`
- `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

Run frontend:

- `cd frontend`
- `npm run dev -- --host 0.0.0.0 --port 3000`

## Exposed ports

- `3000` frontend
- `8000` backend
- `5432` postgres
- `9000` SeaweedFS S3 API
- `9001` SeaweedFS console
