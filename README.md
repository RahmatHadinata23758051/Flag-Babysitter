# Flag Babysitter

[![Validate repository](https://github.com/RahmatHadinata23758051/Flag-Babysitter/actions/workflows/validate.yml/badge.svg)](https://github.com/RahmatHadinata23758051/Flag-Babysitter/actions/workflows/validate.yml)

![Flag Babysitter banner showing three analysis lanes, a coordination bot, and a verified result](assets/flag-babysitter-hero.png)

Evidence-driven Agent Skills for coordinating authorized CTF work, documenting verified solves, and writing repository documentation without unsupported claims.

Flag Babysitter is a source repository for three portable skill directories built around `SKILL.md`. Its core workflow is designed to keep challenge work isolated, limit concurrent workers to three, distinguish candidate flags from independently verified results, and leave submission under user control. It also includes a small offline fixture that exercises the candidate-to-verification boundary without using a live event or real competition artifact.

This repository is a skill source tree, not a standalone CTF application. It includes a tested local installer and an offline validation fixture; it does not claim a universal runtime integration or coverage across real CTF events.

## Contents

- [Why this repository exists](#why-this-repository-exists)
- [What is included](#what-is-included)
- [How the documented workflow fits together](#how-the-documented-workflow-fits-together)
- [Skills](#skills)
- [Compatibility and third-party material](#compatibility-and-third-party-material)
- [Host compatibility](#host-compatibility)
- [Install the skills](#install-the-skills)
- [Use the skills in a CLI agent](#use-the-skills-in-a-cli-agent)
- [Quick verification](#quick-verification)
- [Example run configuration](#example-run-configuration)
- [Synthetic fixture](#synthetic-fixture)
- [Project structure](#project-structure)
- [Safety boundaries](#safety-boundaries)
- [Testing](#testing)
- [Current limitations](#current-limitations)
- [Contributing, security, and license](#contributing-security-and-license)

## Why this repository exists

Multi-challenge CTF work can lose important boundaries when the workflow is informal: a worker may be given too much scope, a plausible flag may be treated as solved without reproduction, or a useful writeup may be produced before the underlying result is established.

The included skills document a narrower workflow for authorized CTF events, training labs, and supplied challenge bundles:

1. Establish the event rules, exact scope, workspace root, and submission policy.
2. Isolate each challenge in its own workspace.
3. Delegate no more than three independent challenges at once, or process them sequentially when subagents are unavailable.
4. Treat worker output as a candidate until a separate verification step reproduces it.
5. Produce a walkthrough only after verification.
6. Hand results to the user; submission is user-controlled by default.

The repository does not claim to solve every category of CTF challenge. It provides orchestration and documentation instructions around a solve process.

## What is included

| Component | Purpose | Evidence |
| --- | --- | --- |
| [`ctf-operator`](skills/ctf-operator/SKILL.md) | Coordinates an authorized CTF workflow, workspace isolation, worker limits, verification, and handoff. | [Skill entrypoint](skills/ctf-operator/SKILL.md) |
| [`ctf-writeup-custom`](skills/ctf-writeup-custom/SKILL.md) | Creates a detailed walkthrough from independently verified evidence. | [Skill entrypoint](skills/ctf-writeup-custom/SKILL.md) |
| [`evidence-readme`](skills/evidence-readme/SKILL.md) | Audits a repository before authoring a README and distinguishes verified facts from inference. | [Skill entrypoint](skills/evidence-readme/SKILL.md) |
| Hero banner | Original project artwork visualizing the documented analysis-to-verification workflow. | [PNG asset](assets/flag-babysitter-hero.png) |
| Synthetic fixture | Provides an offline candidate/verification example using only Python's standard library. | [Fixture](fixtures/synthetic-ctf/base64-proof/README.md) and [benchmark](benchmarks/synthetic-base64-proof.md) |
| Run configuration example | Documents the intended fields for an authorized run. It is not executable configuration. | [Example YAML](examples/run-config.yaml) |

## How the documented workflow fits together

The following flow is derived from the documented `ctf-operator` workflow and its optional handoff to `ctf-writeup-custom`.

```mermaid
flowchart TD
  A["Rules, allowed scope, and challenge material"] --> B["ctf-operator"]
  B --> C["Isolated challenge workspace"]
  C --> D["Worker queue: 1–3 concurrent workers"]
  D --> E["Candidate result"]
  E --> F["Independent verification"]
  F -->|verified| G["ctf-writeup-custom (optional)"]
  F -->|not reproduced| H["Candidate or blocked report"]
  G --> I["User handoff"]
  H --> I
  I --> J["User-controlled submission"]
```

The diagram is a workflow contract, not a claim that the repository runs an agent runtime itself. The skill text requires a single-agent queue when subagents are unavailable, so the same verification boundary remains in place without concurrent workers.

### Candidate versus verified

The distinction between these states is central to the repository:

```mermaid
stateDiagram-v2
  [*] --> Blocked: missing rule, artifact, or dependency
  [*] --> Candidate: worker reports evidence
  Candidate --> Verified: independent reproduction succeeds
  Candidate --> Blocked: evidence cannot be reproduced
  Verified --> [*]: handoff with proof
  Blocked --> [*]: report remaining gap
```

`verified` means that a separate command, original artifact, scoped service, or supplied verifier reproduced the result. It does not mean a platform accepted a submitted flag; acceptance needs a separate platform response.

![Conceptual illustration of an amber candidate artifact passing through an independent fingerprint verification gate before becoming a cyan verified result](assets/candidate-verification-concept.png)

*Conceptual illustration of the documented candidate-to-verification boundary. The Mermaid state diagram and the fixture remain the authoritative workflow evidence.*

## Skills

### `ctf-operator`

[`skills/ctf-operator/SKILL.md`](skills/ctf-operator/SKILL.md) is the orchestration entrypoint. It requires an authorized event or lab, explicit scope, event rules, a workspace root, and a user-controlled submission policy. Its supporting references provide:

- a [run contract](skills/ctf-operator/references/run-contract.md) for the facts that must be established before work starts;
- a [worker task card](skills/ctf-operator/references/worker-task-card.md) that bounds each assignment and report;
- an [evidence ledger](skills/ctf-operator/references/evidence-ledger.md) that records candidates separately from independent verification;
- a [skill-routing guide](skills/ctf-operator/references/skill-routing.md) that selects a primary worker template and optional installed skills;
- [portable worker templates](skills/ctf-operator/references/worker-templates/) for crypto, pwn, reverse, web, forensics, malware, OSINT/misc, AI/ML, and systems challenges;
- [portable environment guidance](skills/ctf-operator/references/environment.md) that avoids machine-specific paths;
- [category guidance](skills/ctf-operator/references/category-guidance.md) for routing without requiring external skill packs; and
- an [optional integration policy](skills/ctf-operator/references/integrations.md) for already-installed specialist skills.

The skill is written to remain useful without a third-party skill pack, a specific virtual environment, or a personal challenge template.

## Compatibility and third-party material

Bundled templates are the fallback when a user does not already have a relevant specialist skill. A user- or event-supplied template takes priority for that event, while already-installed third-party skills can only be focused supplements. Flag Babysitter does not copy those skills into this repository or make them a dependency.

See the [compatibility policy](docs/compatibility.md) for the routing order, licensing boundary, and contribution rule for external material.

## Host compatibility

The repository follows the folder-based Agent Skills shape: each skill has a `SKILL.md` manifest and may include references, scripts, and assets. It is not tied to a single AI CLI. The [host compatibility guide](docs/host-compatibility.md) separates the directory layouts documented by vendors from behavior this repository tests locally.

### `ctf-writeup-custom`

[`skills/ctf-writeup-custom/SKILL.md`](skills/ctf-writeup-custom/SKILL.md) is intentionally downstream of verification. It asks for evidence, solver paths, environment details, and publication constraints before writing.

![Conceptual illustration of verified evidence flowing into a reproducible technical document with code, mathematics, and workflow elements](assets/evidence-to-writeup-concept.png)

*Conceptual illustration of the documentation handoff. It represents the writing contract; it does not depict a runtime component or a completed challenge.*

Its [style reference](skills/ctf-writeup-custom/references/style.md) supports:

- reasoning-led headings instead of a generic report outline;
- reproducible solver commands and dependency notes;
- Mermaid diagrams when they clarify a real flow or state;
- Markdown LaTeX for crypto derivations; and
- a final evidence/link/code check before handoff.

It does not submit flags, interact with a challenge service, or invent missing proof.

### `evidence-readme`

[`skills/evidence-readme/SKILL.md`](skills/evidence-readme/SKILL.md) is a separate documentation skill. Before editing a repository README, it requires a read-only audit covering source structure, entry points, tests, visible documentation, and safe metadata.

Its [audit template](skills/evidence-readme/references/audit-report.md) records verified facts, conservative inferences, and unavailable information. This README was authored under that contract.

## Install the skills

The repository includes a local installer that copies the three skill directories to a parent skill directory you choose. It does not download dependencies or alter an existing skill unless `--force` is provided.

```bash
git clone https://github.com/RahmatHadinata23758051/Flag-Babysitter.git
cd Flag-Babysitter
bash scripts/install.sh --dest /absolute/path/to/your/skills
```

If the destination already contains a same-name skill, installation stops without changing it. An explicit replacement preserves the old skill in a timestamped backup inside the destination:

```bash
bash scripts/install.sh --dest /absolute/path/to/your/skills --force
```

Choose a native skill location for your CLI agent. The installer is tested against a temporary destination by the repository validator; it is not run automatically against a user's local skill directory.

The synthetic fixture test requires:

- Bash;
- Python 3; and
- standard-library modules `base64`, `hashlib`, `pathlib`, and `re`.

No third-party Python dependency is used by the fixture test. The installer deliberately requires an explicit destination instead of assuming a global agent-specific path; this keeps installation scoped to the directory chosen by the user.

## Use the skills in a CLI agent

The canonical content is each skill's `SKILL.md`; the three `agents/openai.yaml` files are optional OpenAI interface metadata. A compatible host may ignore that metadata and still use the skill instructions, references, and scripts.

| CLI agent | Documented skill location or workflow | Example for this repository |
| --- | --- | --- |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | User skills: `~/.gemini/skills/` or `~/.agents/skills/`; workspace skills: `.gemini/skills/` or `.agents/skills/`. | `bash scripts/install.sh --dest .agents/skills` for a workspace install. |
| [Cursor](https://cursor.com/docs/skills) | Discovers `.agents/skills/`, `.cursor/skills/`, and compatible Codex/Claude directories. | `bash scripts/install.sh --dest .agents/skills` for a workspace install. |
| [Claude Code](https://code.claude.com/docs/en/skills) | Uses skills for reusable on-demand workflows; project skills use the `.claude/skills/<name>/SKILL.md` layout. | `bash scripts/install.sh --dest .claude/skills` for a workspace install. |
| [OpenAI skill runtimes](https://developers.openai.com/api/docs/guides/tools-skills) | Discover skill directories through the host's configured capability or skill directories. | Copy the skill folders to the configured parent directory, or upload one skill folder per bundle where the host requires it. |

Run the command only for the host and scope you intend to configure. The generic installer proves that it copies the complete directory structure; it does **not** prove that every version or configuration of every CLI discovers skills in the same way.

Read the [host compatibility guide](docs/host-compatibility.md) before using an unlisted host or a cloud/remote worker.

After installation, ask the agent to use the named skill. Give it only material and endpoints authorized for the event or repository task; do not put credentials or unredacted live flags in the prompt.

```text
Use the ctf-operator skill to coordinate this authorized CTF challenge set. The workspace is ./workspace, the rules are attached, worker count is 2, and submission remains user-controlled.
```

```text
Use the ctf-writeup-custom skill to turn this independently verified solve and its solver path into a reproducible Markdown walkthrough. Do not submit anything.
```

```text
Use the evidence-readme skill to audit this repository read-only before proposing an evidence-backed README revision. Do not run the application or inspect secret files.
```

These examples are prompts, not commands executed by this repository. Exact UI syntax varies by host: for example, Claude Code and Cursor document slash-style skill invocation, while Gemini CLI documents skill discovery and agent activation. The skills can also be selected automatically when the host supports it and their trigger conditions match.

## Quick verification

Run the deterministic local fixture test from the repository root:

```bash
python scripts/validate_repo.py
```

Expected success output:

```text
synthetic fixture: PASS
repository validation: PASS
```

This command checks skill metadata and local links, runs the worker-side solver and independent verifier, and tests the installer's no-overwrite and backup behavior in a task-local temporary directory. It does not access a challenge service, use credentials, install dependencies, or submit anything.

## Example run configuration

[`examples/run-config.yaml`](examples/run-config.yaml) is an illustrative configuration document. The skills do not parse or execute it automatically.

```yaml
event:
  name: Example Training CTF
  workspace_root: ./workspace
scope:
  artifacts_only: true
  endpoints: []
workers:
  requested: 2 # valid range: 1-3
submission:
  mode: user-controlled
```

The documented fields are:

| Field | Meaning |
| --- | --- |
| `event.name` | Human-readable event or lab name. |
| `event.workspace_root` | Parent directory for isolated challenge workspaces. |
| `scope.artifacts_only` | Indicates an offline-only run in the example. |
| `scope.endpoints` | Explicit endpoint allowlist when remote targets are permitted. |
| `workers.requested` | Requested worker count; the operator contract limits it to 1–3. |
| `submission.mode` | Defaults to `user-controlled` in the example. |
| `writeup` | Documents whether to generate a writeup after verification and its output preferences. |
| `environment` | Documents optional activation commands; no path is assumed by the skills. |

## Synthetic fixture

The [Base64 Proof fixture](fixtures/synthetic-ctf/base64-proof/README.md) is a deliberately small offline challenge. It exists to demonstrate a single narrow guarantee: generating a candidate and verifying it are separate operations.

```mermaid
flowchart LR
  A["artifact.txt"] --> B["worker-solution.py"]
  B --> C["Candidate flag"]
  A --> D["verify.py"]
  D --> E["Artifact digest + verified result"]
  C --> E
```

The verifier does not import the worker solver. It checks the original artifact's SHA-256 digest, independently decodes the payload, validates the synthetic flag format, and compares the deterministic expected result. The full scope, reproduction command, and limits are documented in the [synthetic benchmark](benchmarks/synthetic-base64-proof.md).

This fixture does not measure success on real events, network services, other challenge categories, or external subagents.

## Project structure

```text
.
├── assets/
│   ├── candidate-verification-concept.png # Candidate-to-verification illustration
│   ├── evidence-to-writeup-concept.png    # Evidence-to-writeup illustration
│   └── flag-babysitter-hero.png           # Original README hero artwork
├── benchmarks/
│   └── synthetic-base64-proof.md       # Evidence and limits of the fixture run
├── docs/
│   ├── compatibility.md                 # External-skill licensing and precedence
│   └── host-compatibility.md            # Documented CLI host layouts and limits
├── examples/
│   └── run-config.yaml                 # Illustrative run fields
├── fixtures/
│   └── synthetic-ctf/base64-proof/     # Offline artifact, solver, and verifier
├── skills/
│   ├── ctf-operator/                   # Authorized CTF orchestration skill
│   ├── ctf-writeup-custom/             # Verified-solve writeup skill
│   └── evidence-readme/                # Audit-first README authoring skill
├── scripts/
│   ├── install.sh                       # Explicit-destination skill installer
│   └── validate_repo.py                 # Dependency-free repository validator
├── tests/
│   └── validate-synthetic-fixture.sh    # Fixture test runner
├── CONTRIBUTING.md                      # Contribution boundaries and checks
├── LICENSE                              # MIT license for repository-owned content
└── SECURITY.md                          # Safety and vulnerability reporting policy
```

## Safety boundaries

The skills document the following boundaries:

- operate only on supplied artifacts and explicitly allowed CTF/lab endpoints;
- keep credentials as user-controlled runtime secrets and exclude them from files, logs, and worker prompts;
- avoid probing unrelated infrastructure, account enumeration, rate-limit evasion, persistence, or real-world targets outside the event scope;
- prefer offline or read-only work and use bounded remote requests when an event allows them;
- keep submission under explicit user authorization; and
- distinguish local verification from platform acceptance.

These are documented workflow constraints, not a formal security audit or a guarantee that every dependent tool is secure.

## Testing

The repository includes one dependency-free validation command:

```bash
python scripts/validate_repo.py
```

It checks skill metadata and local Markdown links, runs the expected worker candidate output and independent verifier, and validates installer safety in a temporary task-local directory. The validation command was run while preparing this README and returned `repository validation: PASS`.

GitHub Actions runs this same validation on pushes and pull requests targeting `main`. No coverage, live-event integration test, or end-to-end agent-runtime test is present.

## Current limitations

- This is a source tree for skill instructions, not a standalone CTF application.
- Installation copies source skill directories; it does not resolve optional third-party skill packs.
- The executable validation uses a small offline synthetic fixture.
- No benchmark demonstrates performance on real CTF challenges, remote services, all categories, or agent runtimes.
- The example YAML is descriptive and is not parsed by code in this repository.
- Compatibility documentation covers selected Agent Skills hosts; it is not an end-to-end test matrix for every CLI version or cloud worker.
- There is no benchmark for real CTF performance.

## Contributing, security, and license

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Read [SECURITY.md](SECURITY.md) for safety boundaries and responsible reporting. Repository-owned content is available under the [MIT License](LICENSE).

For now, proposed changes should preserve the repository's central distinction between scoped work, candidate results, independently verified results, and user-controlled submission.
