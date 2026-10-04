# Backend Overview

This folder contains the FastAPI backend scaffold for the MVP.

## Current Stack

- FastAPI for the HTTP API and static root response.
- Uvicorn as the ASGI server.
- Pytest for backend smoke and unit tests.

## Main Entry Points

- [app/main.py](app/main.py) defines the FastAPI app, the hello-world root route, and the health endpoint.
- [requirements.txt](requirements.txt) declares the runtime and test dependencies.

## Test Layout

- Backend tests live in [tests/](tests/).

## Current Behavior

- `GET /` returns a simple hello-world HTML page.
- `GET /health` returns `{"status": "ok"}`.

## Working Notes

- Keep the backend thin during the scaffold phase.
- Add persistence and API routes in later phases only after the plan advances.