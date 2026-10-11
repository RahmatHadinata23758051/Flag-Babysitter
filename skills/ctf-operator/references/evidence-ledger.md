# Evidence ledger

Use one ledger per challenge to make the distinction between a worker claim and an independently verified result auditable. Keep it in the challenge workspace, for example at `notes/evidence-ledger.md`. Do not put credentials, live flags, or sensitive service responses in the ledger.

```markdown
# <challenge title> evidence ledger

## Scope snapshot

- Event/lab:
- Challenge ID and category:
- Allowed artifact(s) or endpoint(s):
- Artifact identity (name and digest when practical):
- Rule or request-limit notes:

## Candidate records

| ID | Worker/source | Redacted claim | Evidence location | Reproduction command | Status |
| --- | --- | --- | --- | --- | --- |
| C-001 |  |  |  |  | candidate \| rejected \| verified |

## Verification records

| Candidate ID | Independent verifier | Method | Observed non-sensitive output | Status | Remaining uncertainty |
| --- | --- | --- | --- | --- | --- |
| C-001 |  |  |  | verified \| not reproduced |  |

## Handoff

- Solver path:
- Verification artifact or command:
- Writeup path, if requested:
- Submission status: not authorized \| user-controlled \| submitted with explicit authorization
```

`Redacted claim` identifies the result or hypothesis without storing a live flag. Store any sensitive candidate only in the user-controlled challenge workspace when event rules permit it, not in a shared ledger or public writeup.

Only mark a candidate `verified` after a verifier separate from the originating worker or a supplied deterministic verifier reproduces it. A platform acceptance response, when present, is recorded separately from verification.
