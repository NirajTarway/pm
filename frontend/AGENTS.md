# Frontend Overview

This folder contains the current Next.js Kanban demo.

## Current Stack

- Next.js App Router with React 19 and TypeScript.
- DnD handled with `@dnd-kit`.
- Styling is driven by Tailwind CSS utilities and CSS variables from the app globals.
- Tests use Vitest for unit coverage and Playwright for end-to-end coverage.

## Main Entry Points

- [src/app/page.tsx](src/app/page.tsx) renders the board page.
- [src/components/KanbanBoard.tsx](src/components/KanbanBoard.tsx) owns board state and drag-and-drop behavior.
- [src/lib/kanban.ts](src/lib/kanban.ts) defines the board data model and helper functions.

## Component Structure

- [src/components/KanbanColumn.tsx](src/components/KanbanColumn.tsx) renders a column and its cards.
- [src/components/KanbanCard.tsx](src/components/KanbanCard.tsx) renders an individual card.
- [src/components/KanbanCardPreview.tsx](src/components/KanbanCardPreview.tsx) renders the drag overlay preview.
- [src/components/NewCardForm.tsx](src/components/NewCardForm.tsx) handles adding a new card.

## Test Layout

- Unit tests live beside the implementation in `src/components/` and `src/lib/`.
- End-to-end tests live in [tests/](tests/).
- Vitest setup is in [vitest.config.ts](vitest.config.ts).
- Playwright setup is in [playwright.config.ts](playwright.config.ts).

## Current Behavior

- The homepage renders the Kanban board directly.
- Board state is currently local to the client component.
- Cards can be dragged between columns.
- Columns can be renamed.
- New cards can be added and existing cards can be deleted.

## Working Notes

- Keep changes small and match the existing demo style unless the task explicitly changes the UI direction.
- Prefer testing board helpers and user-visible behavior before broad refactors.