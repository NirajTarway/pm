# Project Onboarding Plan

This plan is for a new teammate who needs to understand the project quickly without guessing.

## What This Project Is

The app is a local Project Management MVP with two current layers:

- A Next.js Kanban demo in `frontend/`.
- A thin FastAPI backend in `backend/` that currently serves a hello-world page and a health check.

The longer-term goal, described in `docs/PLAN.md`, is to move from the demo board to a Dockerized app with login, persistence, and AI-assisted board updates.

## Learning Order

### 1. Run the app end to end

Start here so you can see the current behavior before reading code.

- Read `scripts/AGENTS.md` for the local start and stop flow.
- Read `backend/AGENTS.md` and `frontend/AGENTS.md` for the current runtime boundaries.
- Open the app and confirm the current homepage and backend health route.

What you should be able to answer after this step:

- What runs in Next.js.
- What runs in FastAPI.
- Which part of the app is still demo-only.

### 2. Understand the Kanban data model

Read the shared board model first, because everything in the UI depends on it.

- Read `frontend/src/lib/kanban.ts`.
- Focus on `BoardData`, `Column`, `Card`, `initialData`, and `moveCard`.

What you should verify:

- Columns store ordered card ids.
- Cards are stored once in a lookup table.
- Drag and drop is a pure state transformation on the column order.

### 3. Trace the UI from page to components

Read top-down from the page into the board.

- Read `frontend/src/app/page.tsx`.
- Read `frontend/src/components/KanbanBoard.tsx`.
- Read `frontend/src/components/KanbanColumn.tsx`.
- Read `frontend/src/components/KanbanCard.tsx`.
- Read `frontend/src/components/NewCardForm.tsx`.

What you should understand after this step:

- `page.tsx` simply mounts the board.
- `KanbanBoard.tsx` owns the client state and drag-and-drop handlers.
- `KanbanColumn.tsx` renders one column, rename input, add-card form, and its cards.
- `KanbanCard.tsx` handles sortable card behavior and delete actions.
- `NewCardForm.tsx` is the add-card interaction.

### 4. Read the tests as executable documentation

The tests show the intended behavior better than the structure docs alone.

- Read `frontend/src/lib/kanban.test.ts` for board-state rules.
- Read `frontend/src/components/KanbanBoard.test.tsx` for UI behavior.
- Read `frontend/tests/kanban.spec.ts` for the browser-level flow.
- Read `backend/tests/test_main.py` for backend expectations.

What to notice:

- The helper test checks movement rules without React.
- The component test checks rename, add, and delete behavior.
- The Playwright test checks the page renders and cards can move.
- The backend tests only cover the current scaffold routes.

### 5. Understand the backend scaffold

The backend is intentionally thin right now.

- Read `backend/app/main.py`.
- Read `backend/requirements.txt` if you want the dependency set.
- Compare that with `docs/PLAN.md` to see what still needs to be built.

What you should be able to explain:

- Why `/` currently returns a simple HTML page.
- Why `/health` exists.
- Why persistence, auth, and AI are not implemented yet.

### 6. Learn the project roadmap

`docs/PLAN.md` is the phase-by-phase execution plan.

- Start with Phase 2 through Phase 4 to understand the next product milestones.
- Read later phases only after the earlier ones make sense.

What you should get from this file:

- The app is currently in the scaffold stage.
- The next major product step is static frontend delivery.
- Login, persistence, and AI are intentionally deferred.

## Suggested First Week Sequence

1. Run the app locally and click through the board.
2. Read `frontend/src/lib/kanban.ts` and trace one drag-and-drop interaction.
3. Read `frontend/src/components/KanbanBoard.tsx` and follow how state changes flow into the UI.
4. Read the tests and map each one to the behavior it proves.
5. Read `backend/app/main.py` and confirm the backend is only a scaffold.
6. Read `docs/PLAN.md` and match each phase to the current codebase state.

## What To Ask The Team

- Which phase is currently active and approved.
- Whether the Playwright spec should live under `frontend/tests/` or be moved to the repo root.
- Whether the next implementation step should focus on static frontend delivery or backend persistence work.
- What the expected split is between frontend state and backend state once persistence starts.

## Learning Target

You understand the project well enough when you can explain:

- How one card moves from one column to another.
- Where new cards are created and deleted.
- Why the backend currently returns only scaffold responses.
- Which files will change first when the project moves from demo to product.