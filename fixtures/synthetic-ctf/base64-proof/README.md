# Base64 Proof Fixture

This is an offline, synthetic CTF fixture for validating the orchestration contract. It has no network endpoint, credential, or real-event artifact.

## Scope

Only `artifact.txt` is in scope. The expected workflow is:

1. A worker decodes the supplied Base64 payload and reports a candidate flag.
2. A separate verifier checks the original artifact digest and independently decodes it.
3. Only the verifier may mark the result as verified.

`worker-solution.py` and `verify.py` intentionally do not import one another.
