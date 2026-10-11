# Run contract

Before solving, establish the following facts. If a required fact is unavailable, report the gap instead of inferring permission.

| Field | Required meaning |
| --- | --- |
| Event or lab | The named CTF, training lab, or supplied offline bundle. |
| Scope | Exact artifacts and endpoint allowlist. |
| Rules | Request limits, prohibited techniques, collaboration policy, and submission format. |
| Workspace root | Directory where all task-owned material will be kept. |
| Challenges | IDs, titles, categories, descriptions, attachments, and endpoints where known. |
| Worker count | Requested concurrency from one through three. |
| Submission mode | `user-controlled` by default; exact explicit authorization is required to submit. |
| Writeup mode | Disabled, requested after verification, or event-required format. |

## Evidence status

Use these states consistently:

- `blocked`: a missing artifact, rule, environment, or other dependency prevents meaningful progress.
- `candidate`: a likely flag or solve path exists but has not been independently reproduced.
- `verified`: an independent command, original artifact, scoped service, or supplied verifier reproduces the result.

Each verified result records the source artifact or endpoint, reproduction command, observed non-sensitive output, verification method, and remaining uncertainty. Platform acceptance is a separate fact from local verification.
