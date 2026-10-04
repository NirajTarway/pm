# Docker Deployment Overview

This project uses Docker to package and run the backend scaffold locally.

## What Docker Does Here

Docker builds a small Linux container that contains:

- Python 3.12
- the backend dependencies
- the FastAPI app from `backend/app/main.py`

When the container starts, it runs Uvicorn on port `8000`.

## Current Deployment Flow

```mermaid
flowchart TD
  A[Run start script] --> B[docker compose up --build -d]
  B --> C[Docker builds image from Dockerfile]
  C --> D[Install uv and backend dependencies]
  D --> E[Copy backend code into image]
  E --> F[Start uvicorn app.main:app]
  F --> G[Container listens on port 8000]
  G --> H[Host maps localhost:8000 to container:8000]
  H --> I[Open http://localhost:8000]
  I --> J[GET / returns hello-world page]
  I --> K[GET /health returns {"status":"ok"}]
```

## Files Involved

- [Dockerfile](../Dockerfile) defines the image build and startup command.
- [docker-compose.yml](../docker-compose.yml) defines the service and port mapping.
- [scripts/start.ps1](../scripts/start.ps1) starts the stack on Windows.
- [scripts/start.sh](../scripts/start.sh) starts the stack on macOS or Linux.
- [scripts/stop.ps1](../scripts/stop.ps1) stops the stack on Windows.
- [scripts/stop.sh](../scripts/stop.sh) stops the stack on macOS or Linux.
- [scripts/Use-DockerCli.ps1](../scripts/Use-DockerCli.ps1) helps Windows PowerShell find the Docker CLI.
- [backend/app/main.py](../backend/app/main.py) contains the FastAPI routes that run inside the container.

## Step-By-Step Explanation

1. You run a start script.
2. The script changes to the repo root.
3. It calls `docker compose up --build -d`.
4. Docker reads the Dockerfile and creates an image.
5. The image installs backend dependencies from `backend/requirements.txt`.
6. The backend code is copied into the image.
7. The container starts Uvicorn.
8. Docker exposes the container on host port `8000`.
9. Opening `http://localhost:8000` hits the backend root route.

## Important Note

This Docker setup currently packages only the backend scaffold.

The Next.js frontend is not yet part of the container flow. That is planned for later phases in `docs/PLAN.md`.

## Stop Flow

To shut the stack down, the stop scripts run:

```bash
docker compose down
```

That removes the running container but keeps your source code on disk.