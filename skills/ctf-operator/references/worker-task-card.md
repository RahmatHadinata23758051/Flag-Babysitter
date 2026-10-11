# Worker task card

Give every worker a bounded, self-contained task card:

```text
Event/lab and rules:
Allowed scope:
Challenge ID, title, and category:
Workspace:
Evidence ledger path:
Artifacts and endpoint allowlist:
Relevant category guidance or user template:
Primary worker template path:
Supplemental installed skill/reference (if any):
Objective:
Known hypotheses and completed attempts:
Budget and stop condition:
Constraints: no credentials, no submission, no scope expansion.
```

The worker reports:

```text
Status: blocked | candidate | verified-ready
Findings and evidence:
Reproduction steps and command:
Candidate flag (only if evidenced):
Files created:
Candidate record ID in evidence ledger:
Remaining uncertainty:
Checkpoint/progress for long work:
```

`verified-ready` means ready for independent orchestra verification; it is not permission to claim success or submit.
