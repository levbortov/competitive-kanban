# Product vision — Competitive Kanban

**Status:** approved MVP direction | **Owner:** Product Owner | **Updated:** 2026-11-05

## Mission

Build an API-only competitive personal kanban service that measures relative performance on automatically verifiable tasks. The purpose of the project is also to practice rigorous, traceable GitHub-native software delivery.

## Users and main concepts

- Participant: owns a personal task board and Elo rating.
- Personal task: arbitrary participant-created work; **never** awards Elo by itself.
- Catalog challenge: centrally managed, versioned template with deterministic server-side verification, difficulty 1–5 and reference time.
- Attempt: a participant's single official season attempt at a specific challenge; includes server-controlled start/end timestamps and an immutable evaluation.
- Match: one asynchronous comparison between **two distinct participants'** compatible attempts. An attempt may participate in at most one match.
- Rating event: immutable record of one match and its rating effects.
- Leaderboard: ranking derived from ratings; provisional participants with fewer than five completed rated matches are not eligible for the public ranked leaderboard (proposed threshold included in MVP policy).

## Product MVP

1. Personal API-key authentication and participant identity.
2. Personal boards with tasks and lifecycle (Backlog / In Progress / Done).
3. Administrator-maintained, versioned catalog challenges.
4. Server-side JSON-based evaluation (no execution of untrusted user code).
5. Asynchronous matchmaking and Elo changes.
6. History, audit events, leaderboard and OpenAPI documentation.

## Out of scope

Web UI, multiplayer real-time mode, external account integrations, arbitrary code execution, sophisticated fraud detection, rewards convertible to money, distributed microservices, automatic seasonal resets, user-published rated challenges.

## Nonfunctional outcomes

- Modular monolith with domain isolated from FastAPI and database implementations.
- SQLite first; alternative adapters (including MongoDB) can be added without changing domain rules.
- No database schema or ORM type in public domain interfaces.
- Deterministic calculations and idempotent rating processing.
- Reliable, documented development through GitHub issues, PRs, CI, reviews and releases.
