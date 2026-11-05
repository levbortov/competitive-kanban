# Architecture contract (MVP target)

**Status:** target architecture, not implemented until M01.

The application is a **modular monolith** using ports and adapters. FastAPI, storage adapters and authentication transport are external to the domain.

Dependency direction:

    HTTP routes -> application use cases -> domain entities and rules
                       |                           ^
                       v                           |
                 abstract ports  <-----------------+
                       ^
                       |
          SQLite / future MongoDB adapters

Possible future package organization:

    app/
      domain/         # pure entities, value objects, rules (Elo, attempts, matches)
      application/    # orchestration, repository protocols, transactions
      adapters/
        http/         # FastAPI, request/response schemas, auth transport
        persistence/  # sqlite and optional other stores
        verification/ # trusted deterministic challenge evaluators
      bootstrap/      # dependency wiring and configuration

## Invariants

1. Domain packages never import FastAPI, Pydantic persistence models, sqlite3, MongoDB clients or HTTP types.
2. Application workflows depend only on ports/contracts, not a concrete database.
3. Persistence adapters translate storage representations to domain values.
4. A rating match and the two ledger changes must commit atomically or roll back atomically.
5. The domain owns validation and rules; transport schemas validate shapes, not business policy.
6. Matchmaking concurrency and idempotency are tested against each persistence adapter.
7. Cross-module communication uses explicit application contracts. Avoid circular imports and shared mutable global state.

## Planned ports

ParticipantRepository, BoardRepository, TaskRepository, CatalogRepository, AttemptRepository, MatchRepository, RatingLedgerRepository, UnitOfWork, Clock, ChallengeEvaluator, IdentityProvider.

The port names are provisional; add only interfaces actually needed by an implementation slice. MongoDB replacement means new adapters and migration, not a guarantee that transaction/index semantics are identical. Contract tests across adapters are part of M06.

## Chosen stack

Python, FastAPI, SQLite, pytest and GitHub Actions. Docker introduced once there is a runnable service. No UI in MVP. Keep runtime dependencies minimal.
