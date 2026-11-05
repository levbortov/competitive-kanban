# RATING-001 — Competitive rating specification

**Status:** approved MVP rules | **Version:** 1.0 | **Updated:** 2026-11-05

This document is the normative behavior contract for MVP. Changes require an Issue and a versioned decision; do not silently rewrite recorded rating events.

## 1. Definitions and eligibility

Ordinary user-authored tasks do not affect Elo. Only one official attempt per (participant, challenge template, season) can be created. Attempts for challenges in the centrally managed catalog can affect Elo if verified by server-side deterministic evaluators. A challenge defines an immutable version, difficulty in 1..5, reference duration >0 and the evaluator version.

An attempt is measured by the server from issuance to final submission or server-enforced timeout. Client-provided durations or client claims of verification are not trusted. Retries may not restart an official attempt's timer. Any change to challenge parameters or verification requires a new challenge version.

## 2. Efficiency

Quality Q is in [0,100]; normalized velocity V and efficiency P are:

    V = 100 * min(1, T_reference / T_actual)
    P = 0.70 * Q + 0.30 * V

T_actual must be strictly positive; invalid or missing timestamps must not be accepted as a completed rated result. For a timed-out attempt the server records failure with the defined deadline; no undefined ratio is evaluated.

A successful attempt requires Q >= 80. Quality below 80 is a failed attempt. A failed attempt can lose against a successful attempt, regardless of the computed P. If both attempts succeed, compare P. Absolute P difference <= 0.5 is a draw; otherwise the higher P wins. If both fail, do not make a rated match; preserve the attempts without a rating change.

## 3. Matchmaking

Only attempts belonging to distinct participants, the same challenge template + version, difficulty and season can be paired. Both must be unconsumed official attempts; one attempt can be consumed by at most one match.

Search in a persistent queue, using each attempt's waiting age:
- age <24h: allowed Elo difference <=200
- 24h <= age <72h: allowed Elo difference <=400
- age >=72h: any Elo difference.

A pair is eligible when the difference is within the more permissive of the two participants' current windows, so an older waiting attempt is not stranded by the arrival of a new opponent. Among eligible candidates choose the smallest absolute Elo difference; tie-break by earlier queue time, then immutable attempt identifier to guarantee deterministic results.

A failed attempt may be paired only with a successful attempt, never with another failed attempt. A successful attempt may be paired with either. At season close unmatched attempts expire without Elo changes; there is no artificial win against the clock.

Matchmaking must be concurrency-safe, transactional and idempotent. Re-processing the same attempt, match or event must not award Elo twice.

## 4. Elo equation and stakes

All participants start at 1000 Elo. The outcome S for A is 1 on win, 0.5 on draw and 0 on loss. With R_A, R_B before the match:

    E_A = 1 / (1 + 10 ** ((R_B - R_A) / 400))
    delta_A = K * (S_A - E_A)
    delta_B = -delta_A

K is the same for both participants, selected by challenge difficulty:

| Difficulty | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| K | 18 | 21 | 24 | 27 | 30 |

Preserve full working precision in storage; round only for API presentation. Do not impose a minimum Elo floor. The sum of both ratings must be invariant across a match (within defined numerical tolerance).

No direct point rewards for task creation, finishing an ordinary task, high difficulty or waiting in queue.

## 5. History and seasons

Match, participant rating-before/after, Q, V, P, template and evaluator versions, difficulty, selected K and algorithm version are recorded immutably as rating events. Corrections require an explicit compensating event or audited rebuild operation, never hidden mutation.

Seasons are modeled from the start; the MVP does not automatically reset Elo. A participant is displayed as provisional until at least five completed rated matches. Only non-provisional participants appear in the ranked public leaderboard.

## 6. Abuse boundaries

The MVP prevents duplicate attempts, duplicate matches, invalid timing claims and reprocessing; deterministic/generated inputs and private checks mitigate answer sharing. It does **not** claim resistance to sockpuppets, collusion or offline preparation. A full anti-fraud system is outside MVP.

## 7. Required tests for implementation

- Exact efficiency calculation and threshold at Q=80; time normalization and invalid values.
- Draw boundary at 0.5 and all success/failure combinations.
- Every K level and zero-sum invariant, unequal starting ratings, rounding.
- Match eligibility across templates, versions, seasons and the 24h/72h boundaries.
- Stable tie-breaking, concurrent attempts, duplicate submissions and retries.
- One official attempt per challenge per season, timeout and season close.
- Immutable rating event audit data; leaderboard provisional threshold.
