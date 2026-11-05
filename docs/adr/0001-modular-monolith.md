# ADR-0001: Modular monolith with ports and adapters

**Status:** Accepted (approved project direction) | **Date:** 2026-11-05

## Context

The service is deliberately small, but should prove that the domain survives swapping an initial SQLite adapter for another persistence technology.

## Decision

Use a single deployable Python/FastAPI service. Place pure business rules in a domain layer; express dependencies on persistence and verification through application ports. Adapters contain all DB-specific mapping and queries. Do not introduce microservices for MVP.

## Consequences

- Easier isolated tests, fewer runtime components, clearer dependency boundaries.
- More explicit interface/transaction design and mapping code.
- SQLite and MongoDB do not share identical transactional guarantees; adapters must meet behavior contract tests or explicitly document unsupported semantics.

## Alternatives

Tightly coupled CRUD modules would be smaller initially but impede portability. Microservices add operational complexity without solving the current problem.
