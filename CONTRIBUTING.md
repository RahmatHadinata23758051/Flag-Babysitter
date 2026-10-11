# Contributing to Flag Babysitter

Thank you for improving the project. Contributions should make the skills more useful without expanding work beyond authorized CTFs, supplied challenge bundles, or training labs.

## Before opening a pull request

1. Keep changes focused: one behavior, reference, fixture, or documentation improvement per pull request when practical.
2. Do not add real-event artifacts, credentials, private writeups, copied third-party skill content, or material with an unclear license.
3. Preserve the distinction between a candidate result and independent verification.
4. When adding a workflow or category template, explain its scope and fallback behavior.
5. Run the repository validator from the repository root:

   ```bash
   python scripts/validate_repo.py
   ```

## Adding an integration

External skills are optional integrations, not dependencies. Do not vendor their content into this repository. Document the upstream source, license, and what gap it fills; keep all higher-priority event rules and Flag Babysitter boundaries intact.

## Adding a fixture

Fixtures must be synthetic, offline where practical, deterministic, and safe to execute. A fixture should prove a narrow claim with an expected result. Do not present it as a benchmark for real events or all model behavior.
