# Competitive Kanban

Experimental API-only competitive personal kanban board: ordinary personal tasks coexist with catalog challenges that award Elo only after server verification and one asynchronous match.

**Status:** M00 — governance and project setup. There is no application implementation yet.

## Approved foundations

- [Vision](docs/VISION.md)
- [Rating specification RATING-001](docs/RATING-001.md)
- [Governance policy GOVERNANCE-001](docs/GOVERNANCE-001.md)
- [Architecture and boundaries](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)
- [Contributing and review](CONTRIBUTING.md)
- [Architecture Decision Records](docs/adr/README.md)

## Delivery rules

Feature, governance and architectural changes use GitHub Issues, isolated branches and pull requests. Product and governance pull requests **must not be merged without explicit product-owner acceptance**. CI and reviews do not replace that acceptance.

Project board, milestones, labels, branch rules and additional automation are tracked in GitHub Issues while platform administration is configured.

No API endpoints are available until M01/M02. See [M00 tracking issue](https://github.com/levbortov/competitive-kanban/issues/1).
