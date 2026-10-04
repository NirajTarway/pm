# Project Plan

This document is the working plan for the MVP. Keep the scope narrow, prefer simple implementations, and do not start the next phase until the current phase is checked off and approved where noted.

## Working Rules

- Keep each phase self-contained and testable.
- Prefer the smallest change that proves the next milestone.
- Prove a behavior with tests before expanding the surface area.
- Keep README and docs concise.
- Do not begin implementation beyond the current approved phase.

## Phase 1: Plan And Documentation

Goal: turn this document into the execution plan and make the current frontend codebase discoverable.

- [x] Expand this plan into a phase-by-phase checklist with tests and success criteria.
- [x] Create [frontend/AGENTS.md](../frontend/AGENTS.md) describing the existing frontend code, entry points, scripts, and test layout.
- [x] Confirm the plan is consistent with the current repo structure and the MVP constraints in the root [AGENTS.md](../AGENTS.md).
- [x] Present the plan to the user and wait for explicit approval before implementation starts.

Tests / validation:

- Manual review of the plan for completeness and scope alignment.
- Verify the frontend AGENTS file accurately describes the current app structure.

Success criteria:

- The plan is detailed enough to drive implementation without re-discovery.
- The user has approved the plan before any scaffold or product work begins.

Status:

- Phase 1 is complete and approved.

## Phase 2: Scaffolding

Goal: establish the local runtime and a thin backend that can serve a simple local page and a health endpoint.

- [x] Set up the Docker-based runtime for local development and execution.
- [x] Add a FastAPI backend in [backend/](../backend/).
- [x] Add start and stop scripts in [scripts/](../scripts/) for macOS, Windows, and Linux.
- [x] Serve a simple static HTML response at `/` to prove the app starts locally.
- [x] Add a health endpoint for the backend.
- [x] Verify the app can make a basic API call against the backend health endpoint.

Tests / validation:

- Backend startup test or smoke test for `/`.
- Backend health endpoint test.
- Script smoke test for local start and stop flow.

Success criteria:

- The containerized app starts locally.
- Visiting `/` returns a simple hello-world page.
- The backend responds to a health check.

Status:

- Phase 2 scaffold is complete.
- Docker validation could not be run in this environment because the `docker` CLI is not installed.

## Phase 3: Static Frontend Delivery

Goal: serve the existing Kanban demo as a statically built frontend at `/`.

- [ ] Build the frontend as a static artifact.
- [ ] Serve the frontend from the backend when the app is run locally.
- [ ] Keep the current demo Kanban board visible at `/`.
- [ ] Preserve the current board interactions during the static build transition.
- [ ] Add or update tests around the rendered board and key interactions.

Tests / validation:

- Frontend unit tests for board state helpers and components.
- Frontend integration or end-to-end test that verifies the board renders at `/`.
- Build verification for the frontend static output.

Success criteria:

- The app at `/` shows the demo board after a production build.
- Core board interactions still work in the static build.

## Phase 4: Fake Sign In

Goal: require a dummy login before the Kanban board is shown.

- [ ] Add a sign-in screen for the hardcoded credentials `user` / `password`.
- [ ] Prevent access to the Kanban board until the user signs in.
- [ ] Add log out support.
- [ ] Keep the flow simple and local-only.

Tests / validation:

- Test valid login with the dummy credentials.
- Test invalid login rejection.
- Test sign-out returns the user to the login screen.

Success criteria:

- The board is hidden until login succeeds.
- The user can sign in and sign out without refreshing manually.

## Phase 5: Database Design

Goal: define the Kanban data model before implementing persistence.

- [ ] Propose a database schema for users, boards, columns, cards, and conversation data if needed.
- [ ] Save the schema proposal as JSON in the docs area.
- [ ] Document the persistence approach and assumptions.
- [ ] Get user sign-off before writing the production persistence code.

Tests / validation:

- Review the schema for completeness and future multi-user support.
- Confirm the schema matches the current board behavior and MVP scope.

Success criteria:

- The data model is documented and approved.
- The schema is simple enough to implement directly in the backend.

## Phase 6: Backend Persistence And CRUD

Goal: add backend routes for reading and updating the board for a user.

- [ ] Implement backend routes for board read and update operations.
- [ ] Create the local database automatically if it does not exist.
- [ ] Persist board changes for the signed-in user.
- [ ] Keep the API shape small and explicit.

Tests / validation:

- Backend unit tests for each board read/write route.
- Tests that verify database creation on first run.
- Tests for invalid or missing board data handling where relevant.

Success criteria:

- The backend can read and update a board for a user.
- The database is created automatically when missing.

## Phase 7: Frontend Uses Backend

Goal: make the UI a real persistent Kanban client.

- [ ] Replace local-only board state with backend-backed state.
- [ ] Keep the existing interactions for rename, move, add, edit, and delete.
- [ ] Refresh the UI when backend writes succeed.
- [ ] Preserve a clean user experience during load and save operations.

Tests / validation:

- Integration tests covering frontend-to-backend board reads and writes.
- UI tests for persistence across refresh or reload.
- Regression tests for the existing board interactions.

Success criteria:

- Changes made in the UI persist through the backend.
- The board still feels responsive and predictable.

## Phase 8: AI Connectivity

Goal: prove the backend can call OpenRouter successfully.

- [ ] Add backend support for OpenRouter API calls.
- [ ] Verify the configured model is `openai/gpt-oss-120b`.
- [ ] Add a minimal connectivity test using a simple `2+2` prompt.
- [ ] Keep the AI integration isolated from the board logic for now.

Tests / validation:

- A smoke test or integration test that confirms the AI call returns a result.
- A deterministic check for the simple connectivity prompt.

Success criteria:

- The backend can reach OpenRouter and get a valid response.
- The model configuration is correct.

## Phase 9: Structured AI Board Updates

Goal: send the board state and conversation context to the model and accept structured responses.

- [ ] Send the current Kanban JSON with each AI request.
- [ ] Include the user question and conversation history.
- [ ] Define structured outputs for a user response plus an optional board update.
- [ ] Apply board updates only when the structured response asks for them.

Tests / validation:

- Backend tests for request shaping and response parsing.
- Tests for response handling with and without board changes.
- Tests for conversation history inclusion.

Success criteria:

- The AI receives enough context to reason about the board.
- Structured responses can safely update the board when needed.

## Phase 10: AI Sidebar UI

Goal: add a polished chat sidebar that can drive board changes through the structured AI flow.

- [ ] Build the sidebar chat widget in the frontend.
- [ ] Show user and assistant messages clearly.
- [ ] Let the AI trigger Kanban updates through the structured backend response.
- [ ] Refresh the UI automatically when the board changes.
- [ ] Keep the UI visually aligned with the existing Kanban experience.

Tests / validation:

- UI tests for opening chat, sending a message, and rendering responses.
- Integration tests that verify board refresh after an AI-driven update.
- Regression tests for the existing board interactions after the sidebar is added.

Success criteria:

- The user can chat with the AI from the sidebar.
- AI-directed board edits appear automatically in the UI.

## Approval Gate

Do not begin Phase 2 until the user has reviewed and approved this plan.