# Proposed milestone roadmap

Only M00 has been started. Labels, GitHub Projects and real GitHub Milestones must be configured/verified separately; the entries below are **not** claims of their creation.

| Milestone | Outcome |
|---|---|
| M00 — Governance | Vision, approved rating rules, ADR process, issue/PR templates, baseline CI, GitHub project/rules setup |
| M01 — Foundation | Python project, FastAPI health, adapter interfaces, dependency boundary checks, unit/integration CI |
| M02 — Kanban | Identity, personal boards, task lifecycle, REST/OpenAPI contracts |
| M03 — Evaluation | Versioned challenge catalog, attempts, deterministic evaluation, time tracking |
| M04 — Competition | Matchmaking queue, Elo ledger, provisional leaderboard, concurrency-safe tests |
| M05 — Release | API reference, container package, versioned releases, deployment workflow |
| M06 — Portability | Second persistence adapter, adapter contract tests, migration exercise |

## Project board fields

Status: Backlog, Ready, In Progress, In Review, Acceptance, Done. Separate Blocked flag.
Priority: P0..P3. Size: XS/S/M/L. Area: Governance, Core, API, Persistence, Verification, Rating, DevEx. Iteration is the current timebox.

## M00 exit criteria

A PR contains normative documents and templates; checks pass; manual configuration gaps are tracked; Product Owner accepts governance PR; a trial issue -> PR -> CI -> review -> acceptance -> merge is demonstrated later without bypassing branch rules.
