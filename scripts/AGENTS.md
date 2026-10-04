# Script Overview

This folder contains the cross-platform wrappers for starting and stopping the local Docker stack.

## Current Scripts

- `start.ps1` and `stop.ps1` for Windows PowerShell.
- `start.sh` and `stop.sh` for macOS and Linux shells.
- `Use-DockerCli.ps1` restores the Docker CLI directories to the current PowerShell session PATH.

## Behavior

- Start scripts build and launch the Docker service with `docker compose up --build -d`.
- Stop scripts shut the stack down with `docker compose down`.

## Working Notes

- Keep these scripts aligned with the root Dockerfile and compose file.
- Keep them minimal and avoid extra orchestration logic during the scaffold phase.
- Prefer dot-sourcing `Use-DockerCli.ps1` in project shells when `docker` is not immediately available.