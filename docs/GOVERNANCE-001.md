# GOVERNANCE-001 — GitHub development policy

**Status:** approved for M00 | **Version:** 1.0 | **Updated:** 2026-11-05

## Responsibilities and autonomy

The Product Owner defines product behavior, prioritization, accepts delivery and authorizes merges of product and governance PRs. The implementation agent is responsible for technical design, tests, commits, draft PRs, documentation and follow-up issues within approved scope. A separate review pass or agent can help, but self-review is not represented as independent approval. GitHub Actions supplies objective checks.

There is no autonomous background implementation between user requests. Work is performed in explicitly invoked sessions.

## Source of truth

- Vision and product boundaries: docs/VISION.md.
- Rating rules: docs/RATING-001.md.
- Working agreement: docs/GOVERNANCE-001.md and CONTRIBUTING.md.
- Architectural decisions: docs/adr/.
- Feature requirements and acceptance criteria: GitHub Issues.
- Milestones: release/workstream objectives. GitHub Projects: status, priority, size, iteration, area and views.
- PRs: review evidence, linked issues, implementation reasoning.
- GitHub Actions: reproducible checks. Releases and tags: delivered versions.

## Development state machine

Backlog -> Ready -> In Progress -> In Review -> Acceptance -> Done.

Blocked is an orthogonal condition, not a phase. A new feature begins with discussion and an Issue before code implementation. Sub-issues express decomposition; blocking dependencies are tracked explicitly. Issues must not be called Done before corresponding changes are merged.

### Definition of Ready

Issue explains expected behavior and non-goals, has checkable acceptance criteria, known dependencies, priority and milestone/iteration intent. Significant unknowns are resolved or scoped as spikes.

### Definition of Done

All acceptance criteria satisfied; implementation and required automated tests provided; CI passing; review concerns addressed; contract and architectural docs updated; Product Owner accepts product/governance changes; PR merged; issue closed and project state updated.

## Branches, commits and PRs

- main is the stable integration branch. Bootstrap root commit is the only exception needed to establish an empty repository.
- Changes use isolated branches: feature/*, fix/*, refactor/*, docs/*, chore/*.
- Do not push development changes directly to main after bootstrap.
- Create draft PR while work is unfinished; mark ready after internal checks.
- Link Issue using 'Closes #N' only when this PR fully satisfies it; otherwise use 'Refs #N'.
- Prefer squash merge after CI and review. No force push to protected main.
- **Product, architecture and governance PRs require the Product Owner's explicit acceptance before merge.** M00 PR is covered by this rule. CI success is necessary but not sufficient.
- For minor low-risk maintenance, a lighter acceptance path can be authorized in a later amendment; absent such authorization, do not auto-merge.

## Review and CI

Baseline CI in M00 checks governance structure. Starting M01: formatting, linting, type checking, unit tests, PostgreSQL-independent integration where applicable, API contract tests and architecture boundaries as code is added. Dependabot, CodeQL, secret scanning, releases, Packages, deployments and reusable workflows are introduced with relevant milestones.

Keep workflow permissions least-privilege, pin external actions to full commit SHA, and do not execute privileged actions on untrusted PR code.

## Change control

Changes in product behavior, Elo rules, persistence contracts or architectural dependencies require an Issue, tests and an ADR if a significant design trade-off is involved. Review notes and acceptance decisions must live in the PR timeline. No release from broken main.

## Repository management constraints

Some operations (Projects, Milestones, Labels, Rulesets, repository settings and certain security features) may require owner actions in GitHub settings or an additional connector. Track all manual configuration in Issues and do not claim it is configured until confirmed.
