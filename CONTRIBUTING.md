# Contributing to Competitive Kanban

See [GOVERNANCE-001](docs/GOVERNANCE-001.md) for binding policy.

## Work on an Issue

1. Clarify intended behavior, constraints and acceptance criteria in an Issue.
2. Create a named feature/fix/chore branch and prepare a draft PR.
3. Implement the smallest complete vertical slice; add test evidence.
4. Keep PR description linked to Issue(s); describe impact and migrations.
5. Resolve findings and await CI and Product Owner acceptance before merging product/governance PRs.

## Commit guidelines

Prefer conventional prefixes: feat:, fix:, refactor:, docs:, test:, chore:, ci:. Keep changes small and reversible.

## Pull request readiness

Include scope, acceptance mapping, testing, impact on domain/ports and docs, risks, follow-up tasks. Never claim manual GitHub settings have been enabled unless verified.

## Local M00 checks

Run:

    python3 -m unittest discover -s tests -v

Feature implementation starts in M01. No runtime service or Docker setup exists at M00.
